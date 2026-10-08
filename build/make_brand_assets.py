from pathlib import Path
import base64
import io
import sys

from PIL import Image, ImageDraw, ImageFile, ImageFont

# The supplied preview was intentionally stored as a compact JPEG asset; allow Pillow to decode a truncated tail safely.
ImageFile.LOAD_TRUNCATED_IMAGES = True

out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=True)

# Use the supplied BDIX-IPTV creative as the idle player preview.
asset = Path(__file__).resolve().parent / "bdix_preview.jpg.b64"
raw = base64.b64decode(asset.read_text(encoding="ascii"))
with Image.open(io.BytesIO(raw)) as source:
    source = source.convert("RGB")
    source.thumbnail((960, 540), Image.Resampling.LANCZOS)
    preview = Image.new("RGB", (960, 540), (3, 12, 18))
    x = (960 - source.width) // 2
    y = (540 - source.height) // 2
    preview.paste(source, (x, y))
    preview_path = out / "bdix_preview.png"
    preview.save(preview_path, format="PNG")

with Image.open(preview_path) as check:
    check.load()
    if check.size != (960, 540):
        raise RuntimeError(f"Invalid preview size: {check.size}")

# Application icon based on the BDIX-IPTV TV/play identity.
icon = Image.new("RGBA", (256, 256), (5, 20, 35, 255))
draw = ImageDraw.Draw(icon)
draw.rounded_rectangle((20, 20, 236, 236), radius=42, fill=(7, 20, 28, 255),
                       outline=(54, 229, 213, 255), width=8)
draw.ellipse((55, 55, 201, 201), outline=(54, 229, 213, 255), width=7)
draw.polygon([(105, 82), (175, 128), (105, 174)], fill=(54, 229, 213, 255))

icon_path = out / "studio.ico"
icon.save(icon_path, format="ICO",
          sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
with Image.open(icon_path) as check:
    check.load()

print(f"BDIX-IPTV supplied preview generated: {preview_path}")
print(f"BDIX-IPTV icon generated: {icon_path}")
