"""Recover an intact PNG stream embedded in an SVG data URI.

Only two structural defects are repaired: an incorrect IDAT CRC and a
truncated terminal IEND chunk. Pixel data is never modified. Callers must
still decode the returned PNG fully before accepting it.
"""
from __future__ import annotations

import base64
import binascii
import re
import struct
import zlib

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"\x00\x00\x00\x00IEND\xaeB\x60\x82"
DATA_URI = re.compile(rb'data:image/png;base64,([^"\s]+)', re.IGNORECASE)


def recover_embedded_png_from_svg(svg_bytes: bytes) -> bytes | None:
    """Return a structurally repaired embedded PNG, or None when unsafe."""
    match = DATA_URI.search(svg_bytes)
    if not match:
        return None
    try:
        raw = base64.b64decode(match.group(1), validate=True)
    except (binascii.Error, ValueError):
        return None
    if not raw.startswith(PNG_SIGNATURE):
        return None

    output = bytearray(PNG_SIGNATURE)
    offset = len(PNG_SIGNATURE)
    saw_ihdr = False
    saw_idat = False
    saw_iend = False
    first_chunk = True

    while offset + 8 <= len(raw):
        length = struct.unpack(">I", raw[offset:offset + 4])[0]
        chunk_type = raw[offset + 4:offset + 8]
        data_start = offset + 8
        data_end = data_start + length
        crc_end = data_end + 4
        if crc_end > len(raw):
            # A final IEND chunk may itself be truncated after its length/type
            # or part of its CRC. Accept only a byte-for-byte prefix of IEND.
            if chunk_type == b"IEND" and length == 0 and PNG_IEND.startswith(raw[offset:]):
                output.extend(PNG_IEND)
                saw_iend = True
                offset = len(raw)
                break
            return None

        chunk_data = raw[data_start:data_end]
        saved_crc = struct.unpack(">I", raw[data_end:crc_end])[0]
        actual_crc = zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF
        if saved_crc != actual_crc and chunk_type != b"IDAT":
            return None

        if first_chunk:
            if chunk_type != b"IHDR" or length != 13:
                return None
            saw_ihdr = True
            first_chunk = False
        if chunk_type == b"IDAT":
            saw_idat = True
        if chunk_type == b"IEND":
            if length != 0:
                return None
            saw_iend = True

        output.extend(struct.pack(">I", length))
        output.extend(chunk_type)
        output.extend(chunk_data)
        output.extend(struct.pack(">I", actual_crc))
        offset = crc_end
        if saw_iend:
            break

    if not saw_ihdr or not saw_idat:
        return None

    if not saw_iend:
        tail = raw[offset:]
        # Accept only an exact prefix of the canonical IEND chunk. This avoids
        # silently discarding arbitrary trailing data or a truncated IDAT chunk.
        # Some damaged embedded assets retain the IEND marker and CRC but lose
        # the first one to three zero bytes of its four-byte zero-length field.
        # That suffix is unambiguous because IEND's required data length is zero.
        valid_prefix = PNG_IEND.startswith(tail)
        valid_missing_length_prefix = any(tail == PNG_IEND[offset:] for offset in (1, 2, 3))
        if tail and not (valid_prefix or valid_missing_length_prefix):
            return None
        output.extend(PNG_IEND)
    elif offset != len(raw):
        return None

    return bytes(output)
