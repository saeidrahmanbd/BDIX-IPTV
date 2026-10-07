from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out=Path(sys.argv[1]); out.mkdir(parents=True,exist_ok=True)
W,H=960,540

# BDIX-IPTV idle-preview artwork inspired by the supplied BDIX-IPTV creative:
# dark blue studio scene, strong BDIX-IPTV branding, Bangladesh/India identity,
# and a TV-style category grid. It is generated locally so the portable EXE
# does not need an internet connection just to show its idle screen.
img=Image.new('RGB',(W,H),(4,13,27))
d=ImageDraw.Draw(img)

# Background glow / studio gradient.
for y in range(H):
    t=y/(H-1)
    c=(4+int(4*t), 18+int(13*t), 38+int(28*t))
    d.line((0,y,W,y),fill=c)
glow=Image.new('RGBA',(W,H),(0,0,0,0))
gd=ImageDraw.Draw(glow)
for r,a in [(330,18),(250,24),(180,30)]:
    gd.ellipse((650-r,250-r,650+r,250+r),fill=(0,170,255,a))
glow=glow.filter(ImageFilter.GaussianBlur(45))
img=Image.alpha_composite(img.convert('RGBA'),glow).convert('RGB')
d=ImageDraw.Draw(img)

try:
    bold=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',52)
    sub=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf',24)
    small=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',17)
except Exception:
    bold=sub=small=ImageFont.load_default()

# Brand mark.
d.ellipse((34,28,92,86),fill=(7,21,34),outline=(54,229,213),width=4)
d.polygon([(55,44),(78,57),(55,70)],fill=(54,229,213))
d.text((108,32),'saeidrahmanbd',font=sub,fill=(245,248,252))

d.text((38,112),'BDIX-IPTV',font=bold,fill=(244,248,255))
d.text((40,170),'Bangladesh & India IPTV Hub',font=sub,fill=(240,244,250))
d.text((40,208),'Curated Live TV  •  HD Channels  •  Organized Playlists',font=small,fill=(182,218,244))
d.text((40,234),'Channel Logos  •  Backup Streams  •  EPG Support',font=small,fill=(182,218,244))

# Bangladesh / India identity blocks.
d.rounded_rectangle((40,285,315,345),radius=14,fill=(7,31,43),outline=(30,190,160),width=2)
d.text((58,304),'BANGLADESH',font=small,fill=(75,238,190))
d.rounded_rectangle((40,356,315,416),radius=14,fill=(7,31,43),outline=(48,151,235),width=2)
d.text((58,375),'INDIA  •  HINDI  •  BENGALI',font=small,fill=(100,196,255))

# TV frame.
tv=(430,72,925,405)
d.rounded_rectangle(tv,radius=24,fill=(2,6,12),outline=(67,90,118),width=3)
d.rounded_rectangle((450,92,905,365),radius=12,fill=(8,18,31))
d.text((470,106),'BDIX-IPTV',font=sub,fill=(54,229,213))

# Category cards.
cards=[('Bangladesh',(11,112,91)),('India (Hindi)',(35,128,185)),
       ('India (Bengali)',(211,72,150)),('New Channels',(135,76,220)),
       ('Backup Streams',(89,174,118)),('EPG',(224,154,55))]
x0,y0=468,151
cw,ch=132,84
for i,(label,accent) in enumerate(cards):
    row,col=divmod(i,3)
    x=x0+col*144; y=y0+row*96
    d.rounded_rectangle((x,y,x+cw,y+ch),radius=12,fill=(17,32,49),outline=accent,width=2)
    d.ellipse((x+12,y+14,x+42,y+44),fill=accent)
    d.text((x+50,y+25),label,font=small,fill=(242,246,252))

# TV stand.
d.polygon([(585,405),(775,405),(815,458),(545,458)],fill=(18,25,33))
d.rectangle((525,458,835,470),fill=(12,17,23))

# Footer feature strip.
features=['Organized Categories','Clean Metadata','Local Logos','Backup Streams','EPG Support','Regular Updates']
x=40
for i,label in enumerate(features):
    d.rounded_rectangle((x,485,x+135,520),radius=9,fill=(8,24,37),outline=(45,88,120),width=1)
    d.text((x+10,495),label,font=small,fill=(222,232,241))
    x+=150

img.save(out/'bdix_preview.png','PNG',optimize=True)

# Application icon.
icon=Image.new('RGBA',(256,256),(5,20,35,255))
di=ImageDraw.Draw(icon)
di.rounded_rectangle((20,20,236,236),radius=42,fill=(7,20,28,255),outline=(54,229,213,255),width=8)
di.ellipse((55,55,201,201),outline=(54,229,213,255),width=7)
di.polygon([(105,82),(175,128),(105,174)],fill=(54,229,213,255))
icon.save(out/'studio.ico',format='ICO',sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
print('BDIX-IPTV v5 idle preview and icon generated.')
