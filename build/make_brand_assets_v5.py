from pathlib import Path
import sys
from PIL import Image

out=Path(sys.argv[1])
preview=out/'bdix_preview.png'
if not preview.exists():
    raise RuntimeError(f"Exact BDIX-IPTV preview creative is missing: {preview}")

# Reuse the exact repository creative for the app idle screen.
im=Image.open(preview).convert('RGBA')
im.save(preview,'PNG',optimize=True)

# Derive the application icon from the supplied BDIX-IPTV TV/play mark.
w,h=im.size
crop=im.crop((int(w*.44),int(h*.08),int(w*.63),int(h*.40)))
crop.thumbnail((256,256),Image.Resampling.LANCZOS)
canvas=Image.new('RGBA',(256,256),(5,20,35,255))
canvas.alpha_composite(crop,((256-crop.width)//2,(256-crop.height)//2))
canvas.save(out/'studio.ico',format='ICO',sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
print('Exact BDIX-IPTV creative bundled; icon generated.')
