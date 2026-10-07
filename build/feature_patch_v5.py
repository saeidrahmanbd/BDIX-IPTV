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

# --- Core window/version branding ---
repl('playlist_studio.py',"self.title('Playlist Studio')","self.title('Playlist Studio 5.0')",'window title')
repl('playlist_studio.py',"ttk.Label(body,text='Xtream Codes login'","ttk.Label(body,text='Xtream Codes login'",'Xtream anchor',1)
# Update About/version strings without touching functionality.
p=root/'studio_extras.py'; s=p.read_text(encoding='utf-8')
s=s.replace('PLAYLIST STUDIO  /  2.8.2','PLAYLIST STUDIO 5.0')
s=s.replace('Scan centre · Playlist Studio','Scan centre · BDIX-IPTV / Playlist Studio 5.0')
p.write_text(s,encoding='utf-8')

# --- Multi-category selection + per-view scroll memory ---
p=root/'playlist_studio.py'; s=p.read_text(encoding='utf-8')
s=s.replace("self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.form_dirty=False;",
            "self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.active_groups=[];self.category_scroll={};self.form_dirty=False;",1)
s=s.replace("if self.active_group not in count:self.active_group=None\n            self.groups.selection_set(self.active_group or 'ALL');",
            "valid=[g for g in self.active_groups if g in count] if self.active_groups else ([] if self.active_group is None else [self.active_group] if self.active_group in count else [])\n            self.active_groups=valid;self.active_group=valid[0] if valid else None\n            self.groups.selection_set(valid or 'ALL');",1)
s=s.replace("if self.active_group and ch.category_id!=self.active_group:continue",
            "if self.active_groups and ch.category_id not in self.active_groups:continue\n            if not self.active_groups and self.active_group and ch.category_id!=self.active_group:continue",1)
s=s.replace("self.group_heading.configure(text=self.doc.category(self.active_group).name if self.active_group else 'All channels');",
            "heading=self.doc.category(self.active_groups[0]).name if len(self.active_groups)==1 else (f'{len(self.active_groups)} categories selected' if self.active_groups else (self.doc.category(self.active_group).name if self.active_group else 'All channels'))\n        self.group_heading.configure(text=heading);",1)
# Replace the exact select_group method.
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
if n!=1:raise RuntimeError('select_group replacement failed')
# Add scroll restoration after table rebuild.
anchor="        self.row_logos.set_rows(visible_channels)\n        self.update_scan_summary()"
s=s.replace(anchor,anchor+"\n        key=tuple(self.active_groups) if self.active_groups else ('ALL',)\n        if key in self.category_scroll:\n            try:self.table.yview_moveto(self.category_scroll[key])\n            except Exception:pass",1)
# Primary category editing remains first selected.
s=s.replace("if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;name=simpledialog.askstring('Rename category'",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        name=simpledialog.askstring('Rename category'",1)
s=s.replace("if not self.active_group or not self.resolve_form():return\n        cid=self.active_group;cat=self.doc.category(cid);count=",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        cat=self.doc.category(cid);count=",1)
s=s.replace("if not self.active_group or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==self.active_group);j=i+step",
            "cid=self.active_groups[0] if self.active_groups else self.active_group\n        if not cid or not self.resolve_form():return\n        def change():\n            i=next(i for i,c in enumerate(self.doc.categories) if c.id==cid);j=i+step",1)
# Center the import choice dialog.
s=s.replace("self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.combo.focus_set();parent.wait_window(self)",
            "self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.update_idletasks();parent.update_idletasks();w,h=self.winfo_width(),self.winfo_height();px,py=parent.winfo_rootx(),parent.winfo_rooty();pw,ph=parent.winfo_width(),parent.winfo_height();self.geometry(f'{w}x{h}+{px+(pw-w)//2}+{py+(ph-h)//2}');self.combo.focus_set();parent.wait_window(self)",1)
# Make Xtream import visibly preserve/use the full path.
s=s.replace("c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}")",
            "c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}")",1)
p.write_text(s,encoding='utf-8')

# --- Table sizing / visible EPG + Format columns / larger inspector ---
p=root/'hybrid_ui.py'; s=p.read_text(encoding='utf-8')
s=s.replace("app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url'),show='tree headings',selectmode='extended')",
            "app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url','epg','format'),show='tree headings',selectmode='extended')")
s=s.replace("[('name','Channel',205,135),('group','Group',120,90),('health','Status',105,90),('url','Stream URL',230,110),('epg','EPG ID',100,70),('format','Format',70,60)]",
            "[('name','Channel',220,85),('group','Group',135,60),('health','Status',110,60),('url','Stream URL',420,110),('epg','EPG ID',120,55),('format','Format',85,50)]")
s=s.replace("details=ttk.Frame(app.panes,padding=12,width=430,style='Card.TFrame');app.panes.add(details,weight=1)",
            "details=ttk.Frame(app.panes,padding=12,width=500,style='Card.TFrame');app.panes.add(details,weight=2)")
p.write_text(s,encoding='utf-8')

# --- Larger preview + BDIX placeholder/preview ---
p=root/'studio_extras.py'; s=p.read_text(encoding='utf-8')
s=s.replace("height=280 if compact else 320","height=360 if compact else 400",1)
s=s.replace("self.placeholder=tk.Label(self.video,text='▶\nPLAYLIST STUDIO',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')",
            "self.placeholder=tk.Label(self.video,text='BDIX-IPTV\nPLAYLIST STUDIO 5.0',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
s=s.replace("self.video.bind('<Configure>',lambda e:self.update_view())",
            "self.video.bind('<Configure>',lambda e:self.update_view())",1)
s=s.replace("if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False",
            "if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False;self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
s=s.replace("elif item[0]=='error':self.note.configure(text=item[2])",
            "elif item[0]=='error':self.note.configure(text=item[2]);self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
s=s.replace("self.channel=copy.deepcopy(channel);self.generation+=1;self.name.configure(text=channel.name);self.note.configure(text='Connecting…');self.placeholder.place_forget()",
            "self.channel=copy.deepcopy(channel);self.generation+=1;self.name.configure(text=channel.name);self.note.configure(text='Connecting…');self.placeholder.place_forget()",1)
s=s.replace("def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False",
            "def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False;self.placeholder.place(relx=.5,rely=.5,anchor='center')",1)
p.write_text(s,encoding='utf-8')

print('v5.0 feature patch completed')

# Playlist Studio 5.0 GitHub portable build trigger.
