from pathlib import Path
import re,sys

root=Path(sys.argv[1])
if not root.exists(): raise RuntimeError(f"Source directory not found: {root}")

def read(rel):
    p=root/rel
    if not p.exists(): raise RuntimeError(f"Required source file missing: {p}")
    return p,p.read_text(encoding='utf-8')

def write(p,s): p.write_text(s,encoding='utf-8')

# Identity text.
for rel in ('playlist_studio.py','studio_extras.py','hybrid_ui.py'):
    p,s=read(rel)
    for old in ('Playlist Studio 2.8.2','Playlist Studio 3.0','Playlist Studio 4.0'):
        s=s.replace(old,'Playlist Studio 5.0')
    s=s.replace('PLAYLIST STUDIO  /  3.0','BDIX-IPTV  /  PLAYLIST STUDIO 5.0')
    write(p,s)

# Main application state: multiple categories + remembered table scroll.
p,s=read('playlist_studio.py')
if "self.active_groups=[];self.category_scroll={}" not in s:
    if "self.active_group=None" not in s: raise RuntimeError("active_group initialization not found")
    s=s.replace("self.active_group=None","self.active_group=None;self.active_groups=[];self.category_scroll={}",1)

old="if self.active_group not in count:self.active_group=None\n            self.groups.selection_set(self.active_group or 'ALL');"
new="valid=[g for g in self.active_groups if g in count] if self.active_groups else ([self.active_group] if self.active_group in count else [])\n            self.active_groups=valid;self.active_group=valid[0] if valid else None\n            self.groups.selection_set(valid or 'ALL');"
if old not in s: raise RuntimeError("refresh selection block not found")
s=s.replace(old,new,1)

old="if self.active_group and ch.category_id!=self.active_group:continue"
new="if self.active_groups and ch.category_id not in self.active_groups:continue\n            if not self.active_groups and self.active_group and ch.category_id!=self.active_group:continue"
if old not in s: raise RuntimeError("table category filter not found")
s=s.replace(old,new,1)

old="self.group_heading.configure(text=self.doc.category(self.active_group).name if self.active_group else 'All channels');self.empty.configure"
new="heading=self.doc.category(self.active_groups[0]).name if len(self.active_groups)==1 else (f'{len(self.active_groups)} categories selected' if self.active_groups else 'All channels')\n        self.group_heading.configure(text=heading);self.empty.configure"
if old not in s: raise RuntimeError("group heading block not found")
s=s.replace(old,new,1)

old="self.row_logos.set_rows(visible_channels)\n        self.update_scan_summary()"
new="self.row_logos.set_rows(visible_channels)\n        self.update_scan_summary()\n        key=tuple(self.active_groups) if self.active_groups else ('ALL',)\n        if key in self.category_scroll:\n            try:self.table.yview_moveto(self.category_scroll[key])\n            except Exception:pass"
if old not in s: raise RuntimeError("table refresh anchor not found")
s=s.replace(old,new,1)

pat=r"    def select_group\(self,event=None\):\n.*?^    def select_channel\("
m=re.search(pat,s,re.M|re.S)
if not m: raise RuntimeError("select_group method not found")
new_method="""    def select_group(self,event=None):
        if self.rendering:return
        sel=list(self.groups.selection())
        if not sel:return
        if 'ALL' in sel:
            sel=[]
            self.groups.selection_set('ALL')
        oldkey=tuple(self.active_groups) if self.active_groups else ('ALL',)
        try:self.category_scroll[oldkey]=self.table.yview()[0]
        except Exception:pass
        if not self.resolve_form():
            self.rendering=True;self.groups.selection_set(self.active_groups or 'ALL');self.rendering=False;return
        self.active_groups=sel
        self.active_group=sel[0] if sel else None
        self.refresh_table()
    def select_channel("""
s=s[:m.start()]+new_method+s[m.end():]
write(p,s)

# Main layout.
p,s=read('hybrid_ui.py')
old="app.groups=ttk.Treeview(gb,show='tree',selectmode='browse',style='Category.Treeview');app.groups.column('#0',width=185,minwidth=145)"
new="app.groups=ttk.Treeview(gb,show='tree',selectmode='extended',style='Category.Treeview');app.groups.column('#0',width=185,minwidth=145)"
if old not in s: raise RuntimeError("category Treeview line not found")
s=s.replace(old,new,1)

old="for key,label,width,minimum in [('name','Channel',205,135),('group','Group',120,90),('health','Status',105,90),('url','Stream URL',230,110),('epg','EPG ID',100,70),('format','Format',70,60)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=key in ('name','url'))"
new="for key,label,width,minimum in [('name','Channel',220,140),('group','Group',130,95),('health','Status',110,90),('url','Stream URL',430,180),('epg','EPG ID',100,70),('format','Format',70,60)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=key in ('name','url'))"
if old not in s: raise RuntimeError("table column line not found")
s=s.replace(old,new,1)

old="details=ttk.Frame(app.panes,padding=12,width=430,style='Card.TFrame');app.panes.add(details,weight=1);app.inspector=details"
new="details=ttk.Frame(app.panes,padding=12,width=500,style='Card.TFrame');app.panes.add(details,weight=2);app.inspector=details"
if old not in s: raise RuntimeError("inspector pane line not found")
s=s.replace(old,new,1)

old="left=max(175,min(215,int(width*.15)));right=max(350,min(440,int(width*.29)));app.panes.sashpos(0,left);app.panes.sashpos(1,width-right)"
new="left=max(175,min(215,int(width*.15)));right=max(430,min(540,int(width*.34)));app.panes.sashpos(0,left);app.panes.sashpos(1,width-right)"
if old not in s: raise RuntimeError("pane sizing line not found")
s=s.replace(old,new,1)

old="app.player.video.configure(height=max(150,min(280,app.panes.winfo_height()-300)))"
new="app.player.video.configure(height=max(220,min(420,app.panes.winfo_height()-250)))"
if old not in s: raise RuntimeError("preview height line not found")
s=s.replace(old,new,1)

old="tk.Label(brand,text='Playlist Studio',bg=SIDEBAR,fg=INK,font=('Segoe UI Semibold',15))"
if old in s: s=s.replace(old,"tk.Label(brand,text='BDIX-IPTV  •  Playlist Studio 5.0',bg=SIDEBAR,fg=INK,font=('Segoe UI Semibold',14))",1)
else: raise RuntimeError("header brand label not found")
write(p,s)

# Player preview.
p,s=read('studio_extras.py')
if "height=280 if compact else 320" not in s and "height=360 if compact else 420" not in s:
    raise RuntimeError("player video height line not found")
s=s.replace("height=280 if compact else 320","height=360 if compact else 420",1)

old="""        self.placeholder=tk.Frame(self.video,bg='#03060c',highlightthickness=0)
        self.placeholder_icon=tk.Canvas(self.placeholder,width=78,height=78,bg='#03060c',highlightthickness=0)
        self.placeholder_icon.pack()
        self.placeholder_icon.create_oval(5,5,73,73,outline=ACCENT,width=3)
        self.placeholder_icon.create_polygon(31,22,31,56,54,39,fill=ACCENT)
        self.placeholder_title=tk.Label(self.placeholder,text='PLAYLIST STUDIO',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',20))
        self.placeholder_title.pack(pady=(1,0))
        self.placeholder.place(relx=.5,rely=.5,anchor='center')"""
new="""        self.placeholder=tk.Frame(self.video,bg='#03060c',highlightthickness=0)
        asset=Path(getattr(sys,'_MEIPASS',Path(__file__).resolve().parent))/'bdix_preview.png'
        try:
            self.placeholder_image=ImageTk.PhotoImage(Image.open(asset).convert('RGB'))
            self.placeholder_icon=tk.Label(self.placeholder,image=self.placeholder_image,bg='#03060c',bd=0)
            self.placeholder_icon.pack(fill='both',expand=True)
        except Exception:
            self.placeholder_image=None
            self.placeholder_icon=tk.Canvas(self.placeholder,width=78,height=78,bg='#03060c',highlightthickness=0)
            self.placeholder_icon.pack()
            self.placeholder_icon.create_oval(5,5,73,73,outline=ACCENT,width=3)
            self.placeholder_icon.create_polygon(31,22,31,56,54,39,fill=ACCENT)
            self.placeholder_title=tk.Label(self.placeholder,text='BDIX-IPTV',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',20))
            self.placeholder_title.pack(pady=(1,0))
        self.placeholder.place(relx=.5,rely=.5,anchor='center',relwidth=1,relheight=1)"""
if old not in s: raise RuntimeError("original player placeholder block not found")
s=s.replace(old,new,1)

s=s.replace("def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False",
            "def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False;self.placeholder.place(relx=.5,rely=.5,anchor='center',relwidth=1,relheight=1)",1)
s=s.replace("if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False",
            "if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False;self.placeholder.place(relx=.5,rely=.5,anchor='center',relwidth=1,relheight=1)",1)
s=s.replace("elif item[0]=='error':self.note.configure(text=item[2])",
            "elif item[0]=='error':self.note.configure(text=item[2]);self.placeholder.place(relx=.5,rely=.5,anchor='center',relwidth=1,relheight=1)",1)
if "from PIL import Image, ImageTk" not in s:
    s=s.replace("import tkinter as tk","import tkinter as tk\nfrom PIL import Image, ImageTk",1)
write(p,s)

# Center ChoiceDialog by locating its class in any source file.
found=False
for p in root.rglob('*.py'):
    s=p.read_text(encoding='utf-8')
    if 'class ChoiceDialog' not in s or 'self.grab_set()' not in s: continue
    old='self.grab_set()'
    new="""self.update_idletasks()
        parent.update_idletasks()
        dw,dh=self.winfo_width(),self.winfo_height()
        px,py=parent.winfo_rootx(),parent.winfo_rooty()
        pw,ph=parent.winfo_width(),parent.winfo_height()
        self.geometry(f'{dw}x{dh}+{px+max(0,(pw-dw)//2)}+{py+max(0,(ph-dh)//2)}')
        self.grab_set()"""
    if old not in s: raise RuntimeError(f"{p.name}: ChoiceDialog grab_set missing")
    p.write_text(s.replace(old,new,1),encoding='utf-8')
    found=True
    break
if not found: raise RuntimeError("ChoiceDialog class not found")

print("Playlist Studio 5.0.3 UI patch applied successfully.")
