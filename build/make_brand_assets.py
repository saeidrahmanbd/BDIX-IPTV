from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

out=Path(sys.argv[1])
out.mkdir(parents=True,exist_ok=True)
W,H=1280,720
im=Image.new("RGB",(W,H),(4,20,38))
d=ImageDraw.Draw(im)
# BDIX-IPTV preview artwork: dark IPTV dashboard/TV aesthetic.
for y in range(H):
    t=y/H
    d.line((0,y,W,y),fill=(int(5+8*t),int(22+10*t),int(43+18*t)))
# glow panels
d.rounded_rectangle((55,45,790,645),radius=28,fill=(7,31,53),outline=(42,111,150),width=2)
d.rounded_rectangle((825,80,1225,605),radius=28,fill=(9,25,43),outline=(43,83,112),width=2)
try:
    bold=ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf",88)
    title=ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf",62)
    sub=ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf",30)
    small=ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf",22)
except:
    bold=title=sub=small=None
d.text((95,95),"BDIX-IPTV",font=bold,fill=(232,248,255))
d.text((100,205),"Bangladesh & India IPTV Hub",font=title,fill=(78,220,255))
d.text((100,300),"Curated Live TV  •  HD Channels  •  Organized Playlists",font=sub,fill=(207,229,241))
d.text((100,350),"Channel Logos  •  Backup Streams  •  EPG Support",font=sub,fill=(207,229,241))
# TV/play mark
tv=(900,160,1150,340)
d.rounded_rectangle(tv,radius=34,outline=(54,229,213),width=10)
d.polygon([(980,210),(980,290),(1050,250)],fill=(54,229,213))
d.line((985,155,950,120),fill=(54,229,213),width=7)
d.line((1065,155,1100,120),fill=(54,229,213),width=7)
d.ellipse((942,111,958,127),fill=(54,229,213));d.ellipse((1092,111,1108,127),fill=(54,229,213))
d.text((875,375),"PLAYLIST STUDIO 3.0",font=title,fill=(238,248,250))
# dashboard cards
cards=[("Bangladesh",(25,160,110)),("India (Hindi)",(35,90,145)),("India (Bengali)",(28,145,95)),("Backup Streams",(105,65,180)),("EPG Support",(215,145,35)),("Channel Logos",(230,55,140))]
for i,(label,accent) in enumerate(cards):
    x=865+(i%2)*175; y=455+(i//2)*70
    d.rounded_rectangle((x,y,x+155,y+52),radius=12,fill=(16,39,59),outline=accent,width=2)
    d.text((x+12,y+14),label,font=small,fill=(235,245,250))
d.text((100,585),"Works with XCIPTV and other Xtream/M3U players",font=small,fill=(130,196,220))
im.save(out/"bdix_preview.png",format="PNG",optimize=True)
# Simple BDIX-IPTV TV/play application icon.
icon=Image.new("RGBA",(256,256),(5,20,35,255));q=ImageDraw.Draw(icon)
q.rounded_rectangle((28,62,228,202),radius=32,outline=(54,229,213,255),width=12)
q.polygon([(100,98),(100,166),(162,132)],fill=(54,229,213,255))
q.line((100,62,78,34),fill=(54,229,213,255),width=8);q.line((156,62,178,34),fill=(54,229,213,255),width=8)
q.ellipse((69,24,85,40),fill=(54,229,213,255));q.ellipse((171,24,187,40),fill=(54,229,213,255))
icon.save(out/"studio.ico",format="ICO",sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
print("Brand assets generated.")
