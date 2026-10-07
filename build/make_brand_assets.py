from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont

out=Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=True)
W,H=960,540
img=Image.new('RGB',(W,H),(3,12,18))
d=ImageDraw.Draw(img)
# BDIX-IPTV branded preview: TV/play mark, name, and Playlist Studio 4.0.
cx,cy=480,190
d.ellipse((cx-82,cy-82,cx+82,cy+82),outline=(54,229,213),width=8)
d.polygon([(cx-25,cy-45),(cx+48,cy),(cx-25,cy+45)],fill=(54,229,213))
try:
    f1=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',48)
    f2=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',30)
except Exception:
    f1=f2=ImageFont.load_default()
for text,y,font in [('BDIX-IPTV',310,f1),('PLAYLIST STUDIO 4.0',375,f2)]:
    box=d.textbbox((0,0),text,font=font)
    d.text(((W-(box[2]-box[0]))/2,y),text,font=font,fill=(54,229,213))
img.save(out/'bdix_preview.png','PNG')

icon=Image.new('RGBA',(256,256),(5,20,35,255))
di=ImageDraw.Draw(icon)
di.rounded_rectangle((20,20,236,236),radius=42,fill=(7,20,28,255),outline=(54,229,213,255),width=8)
di.ellipse((55,55,201,201),outline=(54,229,213,255),width=7)
di.polygon([(105,82),(175,128),(105,174)],fill=(54,229,213,255))
icon.save(out/'studio.ico',format='ICO',sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
print('BDIX-IPTV preview and icon generated.')
