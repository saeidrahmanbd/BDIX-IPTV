from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont

out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=True)

# Generate deterministic, Windows-safe BDIX-IPTV branding assets.
W, H = 960, 540
img = Image.new("RGB", (W, H), (3, 12, 18))
draw = ImageDraw.Draw(img)

cx, cy = W // 2, 190
draw.ellipse((cx - 82, cy - 82, cx + 82, cy + 82), outline=(54, 229, 213), width=8)
draw.polygon([(cx - 25, cy - 45), (cx + 48, cy), (cx - 25, cy + 45)], fill=(54, 229, 213))

font_path = Path("C:/Windows/Fonts/segoeuib.ttf")
try:
    f1 = ImageFont.truetype(str(font_path), 48)
    f2 = ImageFont.truetype(str(font_path), 30)
except OSError:
    f1 = f2 = ImageFont.load_default()

for label, y, font in (
    ("BDIX-IPTV", 310, f1),
    ("PLAYLIST STUDIO 4.0", 375, f2),
):
    box = draw.textbbox((0, 0), label, font=font)
    draw.text(((W - (box[2] - box[0])) / 2, y), label, font=font, fill=(54, 229, 213))

preview = out / "bdix_preview.png"
img.save(preview, format="PNG")
with Image.open(preview) as check:
    check.load()
    if check.size != (W, H):
        raise RuntimeError(f"Invalid preview size: {check.size}")

# Explicitly build a square RGBA icon and write all standard Windows sizes.
icon = Image.new("RGBA", (256, 256), (5, 20, 35, 255))
di = ImageDraw.Draw(icon)
di.rounded_rectangle((20, 20, 236, 236), radius=42, fill=(7, 20, 28, 255),
                     outline=(54, 229, 213, 255), width=8)
di.ellipse((55, 55, 201, 201), outline=(54, 229, 213, 255), width=7)
di.polygon([(105, 82), (175, 128), (105, 174)], fill=(54, 229, 213, 255))

icon_path = out / "studio.ico"
icon.save(
    icon_path,
    format="ICO",
    sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)],
)
with Image.open(icon_path) as check:
    check.load()

print(f"BDIX-IPTV branding generated: {preview}")
print(f"BDIX-IPTV icon generated: {icon_path}")
