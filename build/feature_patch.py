from pathlib import Path
import re,sys
root=Path(sys.argv[1])

def one(p,old,new,name):
    s=p.read_text(encoding='utf-8')
    if old not in s:
        raise RuntimeError(f'{p.name}: {name} pattern not found')
    p.write_text(s.replace(old,new,1),encoding='utf-8')

p=root/'playlist_studio.py'
one(p,"super().__init__();self.title('Playlist Studio')","super().__init__();self.title('BDIX-IPTV / Playlist Studio 4.0')","title")
one(p,"self.current=None;self.active_group=None;self.form_dirty=False;","self.current=None;self.active_group=None;self.active_groups=[];self.category_scroll={};self.form_dirty=False;","state")
one(p,"if self.active_group and ch.category_id!=self.active_group:continue","if self.active_groups and ch.category_id not in self.active_groups:continue","filter")
one(p,"if self.active_group not in count:self.active_group=None\n            self.groups.selection_set(self.active_group or 'ALL')","valid=[g for g in self.active_groups if g in count]\n            self.active_groups=valid\n            self.active_group=valid[0] if valid else None\n            self.groups.selection_set(valid or 'ALL')","refresh selection")
one(p,"self.group_heading.configure(text=self.doc.category(self.active_group).name if self.active_group else 'All channels')","heading=self.doc.category(self.active_groups[0]).name if len(self.active_groups)==1 else (f'{len(self.active_groups)} categories selected' if self.active_groups else 'All channels')\n        self.group_heading.configure(text=heading)","heading")
# Insert scroll restoration immediately before the current-channel refresh in refresh_table.
s=p.read_text(encoding='utf-8')
needle="        if self.current and any(ch.id==self.current for ch in self.doc.channels):"
if needle not in s: raise RuntimeError('refresh restore anchor')
s=s.replace(needle,"        key=tuple(self.active_groups) if self.active_groups else ('ALL',)\n        if key in self.category_scroll:\n            try:self.table.yview_moveto(self.category_scroll[key])\n            except Exception:pass\n"+needle,1)
# Replace select_group function only.
pat=r"    def select_group\(self,event=None\):\n.*?    def select_channel\(self,event=None\):"
new="""    def select_group(self,event=None):
        if self.rendering:return
        sel=list(self.groups.selection())
        if not sel:return
        if 'ALL' in sel:sel=['ALL']
        new=[] if sel==['ALL'] else sel
        if new==self.active_groups:return
        oldkey=tuple(self.active_groups) if self.active_groups else ('ALL',)
        try:self.category_scroll[oldkey]=self.table.yview()[0]
        except Exception:pass
        if not self.resolve_form():
            self.rendering=True;self.groups.selection_set(self.active_groups or 'ALL');self.rendering=False;return
        self.active_groups=new
        self.active_group=new[0] if new else None
        self.refresh_table()
    def select_channel(self,event=None):"""
s2,n=re.subn(pat,new,s,count=1,flags=re.S)
if n!=1: raise RuntimeError('select_group function')
p.write_text(s2,encoding='utf-8')

# Primary category actions.
s=p.read_text(encoding='utf-8')
s=s.replace("self.active_group=self.doc.ensure_category(name)\n        self.commit(change,'Category added.')","self.active_group=self.doc.ensure_category(name);self.active_groups=[self.active_group]\n        self.commit(change,'Category added.')",1)
s=s.replace("def rename_category(self):\n        if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;", "def rename_category(self):\n        cid=self.active_groups[0] if self.active_groups else None\n        if not cid or not self.resolve_form():return",1)
s=s.replace("def delete_category(self):\n        if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;", "def delete_category(self):\n        cid=self.active_groups[0] if self.active_groups else None\n        if not cid or not self.resolve_form():return",1)
s=s.replace("self.doc.categories=[c for c in self.doc.categories if c.id!=cid];self.active_group=None","self.doc.categories=[c for c in self.doc.categories if c.id!=cid];self.active_groups=[g for g in self.active_groups if g!=cid];self.active_group=self.active_groups[0] if self.active_groups else None",1)
s=s.replace("def move_category(self,step):\n        if not self.active_group or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==self.active_group);j=i+step","def move_category(self,step):\n        cid=self.active_groups[0] if self.active_groups else None\n        if not cid or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==cid);j=i+step",1)
p.write_text(s,encoding='utf-8')

# Center ChoiceDialog.
one(p,"self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.combo.focus_set();parent.wait_window(self)","self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.update_idletasks();parent.update_idletasks();w,h=self.winfo_width(),self.winfo_height();px,py=parent.winfo_rootx(),parent.winfo_rooty();pw,ph=parent.winfo_width(),parent.winfo_height();self.geometry(f'{w}x{h}+{px+max(0,(pw-w)//2)}+{py+max(0,(ph-h)//2)}');self.combo.focus_set();parent.wait_window(self)","center dialog")

# Xtream path visibility/import mode.
s=p.read_text(encoding='utf-8')
one(p,"status=tk.StringVar(value='Not connected');ttk.Label(body,textvariable=status,style='Muted.TLabel').pack(anchor='w',pady=12)","status=tk.StringVar(value='Not connected');ttk.Label(body,textvariable=status,style='Muted.TLabel').pack(anchor='w',pady=12);request_var=tk.StringVar(value='Request: —');ttk.Label(body,textvariable=request_var,style='Muted.TLabel',wraplength=560).pack(anchor='w',pady=(0,10))","Xtream request label")
old="""                c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}")
                if messagebox.askyesno('Xtream login','Login successful. Import the provider M3U playlist now?',parent=win):
                    url=xtream_m3u_url(c);self.import_link_url(url,replace=False);win.destroy()"""
new="""                c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;url=xtream_m3u_url(c);status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}");request_var.set(f"Request: {url}")
                mode=self.import_mode()
                if mode:self.import_link_url(url,replace=mode.startswith('Replace'),mode=mode);win.destroy()"""
if old not in s:raise RuntimeError('Xtream login')
s=s.replace(old,new,1)
old2="""    def import_link_url(self,url,replace=False):
        self.status.set('Downloading Xtream playlist…')"""
new2="""    def import_link_url(self,url,replace=False,mode=None):
        if mode is None:mode='Replace current playlist' if replace else self.import_mode()
        if not mode:return
        self.status.set(f'Downloading Xtream playlist… {mode}')"""
if old2 not in s:raise RuntimeError('import_link_url')
s=s.replace(old2,new2,1)
p.write_text(s,encoding='utf-8')

p=root/'hybrid_ui.py'
for old,new in [
("selectmode='browse'","selectmode='extended'"),
("tk.Label(brand,text='Playlist Studio'","tk.Label(brand,text='BDIX-IPTV'"),
("text='HYBRID STUDIO 4.0'","text='PLAYLIST STUDIO 4.0'"),
("text='Hybrid Studio'","text='BDIX-IPTV / Playlist Studio 4.0'"),
("displaycolumns=('name','group','health','url')","displaycolumns=('name','group','health','url','epg','format')"),
("details=ttk.Frame(app.panes,padding=12,width=430,style='Card.TFrame');app.panes.add(details,weight=1)","details=ttk.Frame(app.panes,padding=12,width=500,style='Card.TFrame');app.panes.add(details,weight=2)")
]:
    one(p,old,new,old[:24])
s=p.read_text(encoding='utf-8')
old="for key,label,width,minimum in [('name','Channel',205,135),('group','Group',120,90),('health','Status',105,90),('url','Stream URL',230,110),('epg','EPG ID',100,70),('format','Format',70,60)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=key in ('name','url'))"
new="for key,label,width,minimum in [('name','Channel',220,85),('group','Group',135,60),('health','Status',110,60),('url','Stream URL',420,110),('epg','EPG ID',120,55),('format','Format',85,50)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=True)"
one(p,old,new,'column sizing')

p=root/'studio_extras.py'
one(p,"from pathlib import Path","from pathlib import Path\ntry:\n    from PIL import Image,ImageTk\nexcept ImportError:\n    Image=ImageTk=None","PIL")
one(p,"height=280 if compact else 320","height=360 if compact else 400","preview height")
one(p,"self.placeholder=tk.Label(self.video,text='▶\nPLAYLIST STUDIO',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')","self.preview_source=None;self.preview_image=None\n        preview_path=Path(getattr(sys,'_MEIPASS',Path(__file__).parent))/'bdix_preview.png'\n        self.preview_source=Image.open(preview_path).convert('RGB') if Image is not None and preview_path.exists() else None\n        self.placeholder=tk.Label(self.video,text='BDIX-IPTV\nPLAYLIST STUDIO 4.0',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center');self.show_preview()","preview")
one(p,"self.video.bind('<Configure>',lambda e:self.update_view())","self.video.bind('<Configure>',lambda e:(self.update_preview(),self.update_view()))","preview resize")
marker="    def start_worker(self):"
methods="""    def update_preview(self):
        if self.closed or self.preview_source is None:return
        try:
            w=max(320,self.video.winfo_width());h=max(180,self.video.winfo_height());im=self.preview_source.copy();im.thumbnail((w,h),Image.Resampling.LANCZOS);self.preview_image=ImageTk.PhotoImage(im);self.placeholder.configure(image=self.preview_image,text='');self.placeholder.place(relx=.5,rely=.5,anchor='center')
        except Exception:pass
    def show_preview(self):
        if self.closed:return
        self.placeholder.place(relx=.5,rely=.5,anchor='center');self.update_preview()
"""
s=p.read_text(encoding='utf-8')
if marker not in s:raise RuntimeError('player marker')
p.write_text(s.replace(marker,methods+marker,1),encoding='utf-8')
one(p,"self.note.configure(text='Stopped.');self.paused=False","self.note.configure(text='Stopped.');self.paused=False;self.state=5;self.show_preview()","stop preview")
one(p,"if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False","if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False;self.show_preview()","fatal preview")
one(p,"elif item[0]=='error':self.note.configure(text=item[2])","elif item[0]=='error':self.note.configure(text=item[2]);self.show_preview()","error preview")
one(p,"self.media_length=length\n                    if length>0","self.media_length=length\n                    if self.state in (5,6,7):self.show_preview()\n                    if length>0","end preview")
print('Playlist Studio feature patch applied')
