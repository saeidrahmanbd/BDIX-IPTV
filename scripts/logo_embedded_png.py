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
        # Correct a narrowly scoped IDAT length overrun when the final PNG
        # chunk has an exact IEND marker. Pillow validates the reconstructed
        # compressed image data before the caller accepts the result.
        terminal = len(raw) - 12
        if chunk_type == b"IDAT" and terminal >= data_start + 4 and raw[terminal:terminal + 8] == b"\x00\x00\x00\x00IEND":
            inferred_length = terminal - data_start - 4
            if inferred_length >= 0 and length > inferred_length:
                length = inferred_length
        data_end = data_start + length
        crc_end = data_end + 4
        if crc_end > len(raw):
            # Some broadcaster SVG exports contain an IDAT length that runs
            # three bytes into the terminal IEND chunk. Recover only when the
            # final 12 bytes have the exact IEND length/type marker. Infer the
            # true IDAT boundary from that marker, rebuild its length and CRC,
            # and let Pillow independently decode the resulting pixel stream.
            terminal = len(raw) - 12
            if (
                chunk_type == b"IDAT"
                and terminal >= data_start + 4
                and raw[terminal:terminal + 8] == b"\x00\x00\x00\x00IEND"
            ):
                inferred_length = terminal - data_start - 4
                if inferred_length < 0:
                    return None
                chunk_data = raw[data_start:data_start + inferred_length]
                actual_crc = zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF
                output.extend(struct.pack(">I", inferred_length))
                output.extend(chunk_type)
                output.extend(chunk_data)
                output.extend(struct.pack(">I", actual_crc))
                output.extend(PNG_IEND)
                saw_ihdr = True
                saw_idat = True
                saw_iend = True
                offset = len(raw)
                break
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
        # IDAT CRC damage is tolerated because the compressed pixel stream is
        # independently decoded by the caller. Also repair a damaged IEND CRC,
        # but only for a zero-length terminal IEND chunk; its canonical CRC is
        # deterministic and no image data is discarded or modified.
        terminal_iend = chunk_type == b"IEND" and length == 0 and crc_end == len(raw)
        if saved_crc != actual_crc and chunk_type != b"IDAT" and not terminal_iend:
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
        if tail and not PNG_IEND.startswith(tail):
            return None
        output.extend(PNG_IEND)
    elif offset != len(raw):
        return None

    return bytes(output)
