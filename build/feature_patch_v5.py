from pathlib import Path
import re,sys

root=Path(sys.argv[1])

def repl(path, old, new, label, count=1):
    p=root/path
    s=p.read_text(encoding='utf-8')
    if old not in s:
        raise RuntimeError(f"{path}: required pattern missing: {label}")
    s=s.replace(old,new,count)
    p.write_text(s,encoding='utf-8')

def repl_regex(path, pattern, replacement, label, count=1, flags=re.S):
    p=root/path
    s=p.read_text(encoding='utf-8')
    ns,n=re.subn(pattern,replacement,s,count=count,flags=flags)
    if n < count:
        raise RuntimeError(f"{path}: required regex pattern missing: {label}")
    p.write_text(ns,encoding='utf-8')

# --- Core window/version branding ---
p=root/'playlist_studio.py'
s=p.read_text(encoding='utf-8')
s,n=re.subn(r"self\.title\(['\"]Playlist Studio(?: [0-9.]+)?['\"]\)",
            "self.title('Playlist Studio 5.0')",s,count=1)
if n!=1:
    raise RuntimeError("playlist_studio.py: window title pattern not found")
p.write_text(s,encoding='utf-8')

p=root/'studio_extras.py'
s=p.read_text(encoding='utf-8')
s=s.replace('PLAYLIST STUDIO  /  2.8.2','PLAYLIST STUDIO 5.0')
s=s.replace('BDIX-IPTV  /  PLAYLIST STUDIO 4.0','BDIX-IPTV  /  PLAYLIST STUDIO 5.0')
s=s.replace('Scan centre · Playlist Studio','Scan centre · BDIX-IPTV / Playlist Studio 5.0')
s=s.replace('Scan centre · BDIX-IPTV / Playlist Studio 4.0','Scan centre · BDIX-IPTV / Playlist Studio 5.0')
p.write_text(s,encoding='utf-8')

# --- Multi-category selection + per-view scroll memory ---
p=root/'playlist_studio.py'; s=p.read_text(encoding='utf-8')
s=s.replace("self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.form_dirty=False;",
            "self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.active_groups=[];self.category_scroll={};self.form_dirty=False;",1)

# Explicitly force Ctrl/Shift multi-selection on the category Treeview.
lines=s.splitlines()
for i,line in enumerate(lines):
    if 'self.groups' in line and 'Treeview' in line:
        if 'selectmode=' in line:
            line=re.sub(r"selectmode\s*=\s*['\"][^'\"]+['\"]","selectmode='extended'",line)
        else:
            pos=line.rfind(')')
            if pos<0: raise RuntimeError('playlist_studio.py: category Treeview line has no closing parenthesis')
            line=line[:pos]+",selectmode='extended'"+line[pos:]
        lines[i]=line
        break
else:
    raise RuntimeError('playlist_studio.py: category Treeview creation not found')
s='\n'.join(lines)+'\n'

s=s.replace("if self.active_group not in count:self.active_group=None\n            self.groups.selection_set(self.active_group or 'ALL');",
            "valid=[g for g in self.active_groups if g in count] if self.active_groups else ([] if self.active_group is None else [self.active_group] if self.active_group in count else [])\n            self.active_groups=valid;self.active_group=valid[0] if valid else None\n            self.groups.selection_set(valid or 'ALL');",1)

s=s.replace("if self.active_group and ch.category_id!=self.active_group:continue",
            "if self.active_groups and ch.category_id not in self.active_groups:continue\n            if not self.active_groups and self.active_group and ch.category_id!=self.active_group:continue",1)

s=s.replace("self.group_heading.configure(text=self.doc.category(self.active_group).name if self.active_group else 'All channels');",
            "heading=self.doc.category(self.active_groups[0]).name if len(self.active_groups)==1 else (f'{len(self.active_groups)} categories selected' if self.active_groups else (self.doc.category(self.active_group).name if self.active_group else 'All channels'))\n        self.group_heading.configure(text=heading);",1)

pat=r"    def select_group\(self,event=None\):\n        if self\.rendering:return\n        sel=self\.groups\.selection\(\)\n        if not sel:return\n        new=None if sel\[0\]=='ALL' else sel\[0\]\n        if new==self\.active_group:return\n        if not self\.resolve_form\(\):\n            self\.rendering=True;self\.groups\.selection_set\(self\.active_group or 'ALL'\);self\.rendering=False;return\n        self\.active_group=new;self\.groups\.selection_set\(new or 'ALL'\);self\.refresh_table\(\)"
new="""    def select_group(self,event=None):
        if self.rendering:return
        sel=list(self.groups.selection())
        if not sel:return
        if 'ALL' in sel: sel=[]
        oldkey=tuple(self.active_groups) if self.active_groups else ('ALL',)
        try:self.category_scroll[oldkey]=self.table.yview()[0]
        except Exception:pass
        if not self.resolve_form():
            self.rendering=True;self.groups.selection_set(self.active_groups or 'ALL');self.rendering=False;return
        self.active_groups=sel
        self.active_group=sel[0] if sel else None
        self.refresh_table()"""
s,n=re.subn(pat,new,s,count=1,flags=re.S)
if n!=1: raise RuntimeError('select_group replacement failed')

anchor="        self.row_logos.set_rows(visible_channels)\n        self.update_scan_summary()"
if anchor not in s: raise RuntimeError('table refresh anchor missing')
s=s.replace(anchor,anchor+"\n        key=tuple(self.active_groups) if self.active_groups else ('ALL',)\n        if key in self.category_scroll:\n            try:self.table.yview_moveto(self.category_scroll[key])\n            except Exception:pass",1)

s=s.replace("if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;name=simpledialog.askstring('Rename category'",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        name=simpledialog.askstring('Rename category'",1)
s=s.replace("if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;cat=self.doc.category(cid);count=",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        cat=self.doc.category(cid);count=",1)
s=s.replace("if not self.active_group or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==self.active_group);j=i+step",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==cid);j=i+step",1)

# --- Center import Append/Replace dialog over the main window ---
old="self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.combo.focus_set();parent.wait_window(self)"
new="self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.update_idletasks();parent.update_idletasks();w,h=self.winfo_width(),self.winfo_height();px,py=parent.winfo_rootx(),parent.winfo_rooty();pw,ph=parent.winfo_width(),parent.winfo_height();self.geometry(f'{w}x{h}+{px+(pw-w)//2}+{py+(ph-h)//2}');self.combo.focus_set();parent.wait_window(self)"
if old not in s: raise RuntimeError('import choice dialog anchor missing')
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

# --- Table sizing / larger Stream URL / larger preview inspector ---
p=root/'hybrid_ui.py'; s=p.read_text(encoding='utf-8')
s=s.replace("app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url'),show='tree headings',selectmode='extended')",
            "app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url','epg','format'),show='tree headings',selectmode='extended')",1)
s=s.replace("[('name','Channel',205,135),('group','Group',120,90),('health','Status',105,90),('url','Stream URL',230,110),('epg','EPG ID',100,70),('format','Format',70,60)]",
            "[('name','Channel',220,85),('group','Group',135,60),('health','Status',110,60),('url','Stream URL',420,110),('epg','EPG ID',120,55),('format','Format',85,50)]",1)
s=s.replace("details=ttk.Frame(app.panes,padding=12,width=430,style='Card.TFrame');app.panes.add(details,weight=1)",
            "details=ttk.Frame(app.panes,padding=12,width=500,style='Card.TFrame');app.panes.add(details,weight=2)",1)
p.write_text(s,encoding='utf-8')

# --- Larger preview + real BDIX-IPTV preview image when idle ---
p=root/'studio_extras.py'; s=p.read_text(encoding='utf-8')
s=s.replace("height=280 if compact else 320","height=360 if compact else 400",1)

if "import tkinter as tk" in s and "from pathlib import Path" not in s:
    s=s.replace("import tkinter as tk","import tkinter as tk\nfrom pathlib import Path\nimport sys",1)
elif "from pathlib import Path" not in s:
    s="from pathlib import Path\nimport sys\n"+s

old="self.placeholder=tk.Label(self.video,text='▶\nPLAYLIST STUDIO',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')"
if old not in s:
    old4="self.placeholder=tk.Label(self.video,text='BDIX-IPTV\nPLAYLIST STUDIO 4.0',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')"
    if old4 not in s: raise RuntimeError('placeholder creation line missing')
    old=old4
new="""asset=Path(getattr(sys,'_MEIPASS',Path(__file__).resolve().parent))/'bdix_preview.png'
if not asset.exists(): asset=Path(__file__).resolve().parent/'bdix_preview.png'
try:
    self.placeholder_image=tk.PhotoImage(file=str(asset))
    self.placeholder=tk.Label(self.video,image=self.placeholder_image,bg='#03060c',bd=0)
except Exception:
    self.placeholder_image=None
    self.placeholder=tk.Label(self.video,text='BDIX-IPTV\nPLAYLIST STUDIO 5.0',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23),bd=0)
self.placeholder.place(relx=.5,rely=.5,anchor='center')"""
s=s.replace(old,new,1)
s=s.replace("if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False",
            "if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False;self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
s=s.replace("elif item[0]=='error':self.note.configure(text=item[2])",
            "elif item[0]=='error':self.note.configure(text=item[2]);self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
s=s.replace("def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False",
            "def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False;self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
p.write_text(s,encoding='utf-8')

print('Playlist Studio 5.0 feature patch updated: explicit multi-select, scroll memory, centered import dialog, wider URL/inspector, larger preview, and bundled BDIX preview image.')
