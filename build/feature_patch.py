from pathlib import Path
import re, sys
root=Path(sys.argv[1])

def patch(path, transforms):
    p=root/path; s=p.read_text(encoding="utf-8")
    for name, old, new in transforms:
        n=s.count(old)
        if n != 1: raise RuntimeError(f"{path}: {name}: expected 1 match, got {n}")
        s=s.replace(old,new,1)
    p.write_text(s,encoding="utf-8")
    print("patched",path)

patch("playlist_studio.py",[
("window_title","super().__init__();self.title('Playlist Studio')","super().__init__();self.title('BDIX-IPTV / Playlist Studio 3.0')"),
("state",
"self.doc=Playlist();self.history=History();self.path=None;self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.form_dirty=False;",
"self.doc=Playlist();self.history=History();self.path=None;self.saved=self.doc.fingerprint();self.current=None;self.active_group=None;self.active_groups=[];self.category_scroll={};self.form_dirty=False;"),
("refresh",
"            if self.active_group not in count:self.active_group=None\n            self.groups.selection_set(self.active_group or 'ALL');self.category_combo.configure(values=[c.name for c in self.doc.categories]);self.refresh_table(select)",
"            valid=[g for g in self.active_groups if g in count]\n            self.active_groups=valid;self.active_group=valid[0] if valid else None\n            self.groups.selection_set(valid or 'ALL');self.category_combo.configure(values=[c.name for c in self.doc.categories]);self.refresh_table(select)"),
("filter",
"            if self.active_group and ch.category_id!=self.active_group:continue",
"            if self.active_groups and ch.category_id not in self.active_groups:continue"),
("heading",
"        self.group_heading.configure(text=self.doc.category(self.active_group).name if self.active_group else 'All channels');self.empty.configure(text=f'{shown:,} shown · Select a channel to edit. Ctrl-click or Shift-click for bulk actions.' if shown else 'No matches. Change View, clear search, or run Scan links.' if self.doc.channels else 'Open an M3U file or import a playlist link to start.')\n        self.display_query=self.search.get();self.rendering=was",
"        heading=self.doc.category(self.active_groups[0]).name if len(self.active_groups)==1 else f'{len(self.active_groups)} categories selected' if self.active_groups else 'All channels'\n        self.group_heading.configure(text=heading);self.empty.configure(text=f'{shown:,} shown · Select a channel to edit. Ctrl-click or Shift-click for bulk actions.' if shown else 'No matches. Change View, clear search, or run Scan links.' if self.doc.channels else 'Open an M3U file or import a playlist link to start.')\n        self.display_query=self.search.get();self.rendering=was\n        key=tuple(self.active_groups) if self.active_groups else ('ALL',)\n        if key in self.category_scroll:\n            try:self.table.yview_moveto(self.category_scroll[key])\n            except tk.TclError:pass"),
("select_group",
"""    def select_group(self,event=None):
        if self.rendering:return
        sel=self.groups.selection()
        if not sel:return
        new=None if sel[0]=='ALL' else sel[0]
        if new==self.active_group:return
        if not self.resolve_form():
            self.rendering=True;self.groups.selection_set(self.active_group or 'ALL');self.rendering=False;return
        self.active_group=new;self.groups.selection_set(new or 'ALL');self.refresh_table()
""",
"""    def select_group(self,event=None):
        if self.rendering:return
        sel=list(self.groups.selection())
        if not sel:return
        if 'ALL' in sel: sel=['ALL']
        new=[] if sel==['ALL'] else sel
        if new==self.active_groups:return
        oldkey=tuple(self.active_groups) if self.active_groups else ('ALL',)
        try:self.category_scroll[oldkey]=self.table.yview()[0]
        except tk.TclError:pass
        if not self.resolve_form():
            self.rendering=True;self.groups.selection_set(self.active_groups or 'ALL');self.rendering=False;return
        self.active_groups=new;self.active_group=new[0] if new else None;self.refresh_table()
"""),
("add_category",
"            self.active_group=self.doc.ensure_category(name)\n        self.commit(change,'Category added.')",
"            self.active_group=self.doc.ensure_category(name);self.active_groups=[self.active_group]\n        self.commit(change,'Category added.')"),
("rename_primary",
"""    def rename_category(self):
        if not self.active_group or not self.resolve_form():return
        cid=self.active_group;name=simpledialog.askstring('Rename category','New name:',initialvalue=self.doc.category(cid).name,parent=self)
""",
"""    def rename_category(self):
        cid=self.active_groups[0] if self.active_groups else None
        if not cid or not self.resolve_form():return
        name=simpledialog.askstring('Rename category','New name:',initialvalue=self.doc.category(cid).name,parent=self)
"""),
("delete_primary",
"""    def delete_category(self):
        if not self.active_group or not self.resolve_form():return
        cid=self.active_group;cat=self.doc.category(cid);count=sum(c.category_id==cid for c in self.doc.channels)
""",
"""    def delete_category(self):
        cid=self.active_groups[0] if self.active_groups else None
        if not cid or not self.resolve_form():return
        cat=self.doc.category(cid);count=sum(c.category_id==cid for c in self.doc.channels)
"""),
("delete_state",
"            self.doc.categories=[c for c in self.doc.categories if c.id!=cid];self.active_group=None",
"            self.doc.categories=[c for c in self.doc.categories if c.id!=cid];self.active_groups=[g for g in self.active_groups if g!=cid];self.active_group=self.active_groups[0] if self.active_groups else None"),
("move_primary",
"""    def move_category(self,step):
        if not self.active_group or not self.resolve_form():return
        def change():
            i=next(i for i,c in enumerate(self.doc.categories) if c.id==self.active_group);j=i+step
""",
"""    def move_category(self,step):
        cid=self.active_groups[0] if self.active_groups else None
        if not cid or not self.resolve_form():return
        def change():
            i=next(i for i,c in enumerate(self.doc.categories) if c.id==cid);j=i+step
"""),
("sort_channels",
"""            for cat in self.doc.categories:
                if self.active_group and cat.id!=self.active_group:continue
""",
"""            selected=set(self.active_groups)
            for cat in self.doc.categories:
                if selected and cat.id not in selected:continue
"""),
("choice_center",
"""        self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.combo.focus_set();parent.wait_window(self)
""",
"""        self.bind('<Return>',lambda e:self.accept());self.bind('<Escape>',lambda e:self.destroy());self.grab_set();self.update_idletasks();parent.update_idletasks();w,h=self.winfo_width(),self.winfo_height();px,py=parent.winfo_rootx(),parent.winfo_rooty();pw,ph=parent.winfo_width(),parent.winfo_height();self.geometry(f'{w}x{h}+{px+max(0,(pw-w)//2)}+{py+max(0,(ph-h)//2)}');self.combo.focus_set();parent.wait_window(self)
"""),
("reset_new",
"self.active_group=None;self.history=History();self.saved=self.doc.fingerprint();self.search.set('');",
"self.active_group=None;self.active_groups=[];self.history=History();self.saved=self.doc.fingerprint();self.search.set('');"),
("reset_file",
"self.current=None;self.active_group=None;self.history=History();self.saved=self.doc.fingerprint() if len(paths)==1 else '';",
"self.current=None;self.active_group=None;self.active_groups=[];self.history=History();self.saved=self.doc.fingerprint() if len(paths)==1 else '';"),
("reset_import",
"self.current=None;self.active_group=None;self.history=History();self.saved='';self.health_view.set('All channels');",
"self.current=None;self.active_group=None;self.active_groups=[];self.history=History();self.saved='';self.health_view.set('All channels');"),
("reset_github",
"self.current=None;self.active_group=None;self.scan_results.clear();self.refresh();",
"self.current=None;self.active_group=None;self.active_groups=[];self.scan_results.clear();self.refresh();"),
("xtream_status",
"status=tk.StringVar(value='Not connected');ttk.Label(body,textvariable=status,style='Muted.TLabel').pack(anchor='w',pady=12)",
"status=tk.StringVar(value='Not connected');ttk.Label(body,textvariable=status,style='Muted.TLabel').pack(anchor='w',pady=12);request_var=tk.StringVar(value='Request: —');ttk.Label(body,textvariable=request_var,style='Muted.TLabel',wraplength=560).pack(anchor='w',pady=(0,10))"),
("xtream_login",
"""                c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}")
                if messagebox.askyesno('Xtream login','Login successful. Import the provider M3U playlist now?',parent=win):
                    url=xtream_m3u_url(c);self.import_link_url(url,replace=False);win.destroy()
""",
"""                c=XtreamConfig(**{k:v.get().strip() for k,v in fields.items()});base,data=xtream_login(c);self.xtream_cfg=c;url=xtream_m3u_url(c);status.set(f"Authenticated: {data.get('user_info',{}).get('status','unknown')} — {base}");request_var.set(f"Request: {url}")
                mode=self.import_mode()
                if mode:self.import_link_url(url,replace=mode.startswith('Replace'),mode=mode);win.destroy()
"""),
("import_link_url",
"""    def import_link_url(self,url,replace=False):
        self.status.set('Downloading Xtream playlist…')
        def worker():
            try:self.events.put(('import',fetch_playlist(url),'Replace current playlist' if replace else self.import_mode()))
            except Exception as ex:self.events.put(('error',str(ex)))
        threading.Thread(target=worker,daemon=True).start()
""",
"""    def import_link_url(self,url,replace=False,mode=None):
        if mode is None: mode='Replace current playlist' if replace else self.import_mode()
        if not mode:return
        self.status.set(f'Downloading Xtream playlist… {mode}')
        def worker():
            try:self.events.put(('import',fetch_playlist(url),mode))
            except Exception as ex:self.events.put(('error',str(ex)))
        threading.Thread(target=worker,daemon=True).start()
""")
])

patch("hybrid_ui.py",[
("category_multi","app.groups=ttk.Treeview(gb,show='tree',selectmode='browse',style='Category.Treeview')","app.groups=ttk.Treeview(gb,show='tree',selectmode='extended',style='Category.Treeview')"),
("brand","tk.Label(brand,text='Playlist Studio',bg=SIDEBAR,fg=INK,font=('Segoe UI Semibold',15)).pack(side='left',padx=9)","tk.Label(brand,text='BDIX-IPTV',bg=SIDEBAR,fg=INK,font=('Segoe UI Semibold',15)).pack(side='left',padx=9)"),
("brand_sub","tk.Label(sidebar,text='HYBRID STUDIO 3.0',bg=SIDEBAR,fg=ACCENT,font=('Segoe UI Semibold',8)).pack(anchor='w',padx=17,pady=(0,9))","tk.Label(sidebar,text='PLAYLIST STUDIO 3.0',bg=SIDEBAR,fg=ACCENT,font=('Segoe UI Semibold',8)).pack(anchor='w',padx=17,pady=(0,9))"),
("top_brand","ttk.Label(left,text='Hybrid Studio',font=('Segoe UI Semibold',20),background=BG).pack(anchor='w')","ttk.Label(left,text='BDIX-IPTV / Playlist Studio 3.0',font=('Segoe UI Semibold',20),background=BG).pack(anchor='w')"),
("columns","app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url'),show='tree headings',selectmode='extended')","app.table=ttk.Treeview(table,columns=('name','group','health','url','epg','format'),displaycolumns=('name','group','health','url','epg','format'),show='tree headings',selectmode='extended')"),
("widths","for key,label,width,minimum in [('name','Channel',205,135),('group','Group',120,90),('health','Status',105,90),('url','Stream URL',230,110),('epg','EPG ID',100,70),('format','Format',70,60)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=key in ('name','url'))","for key,label,width,minimum in [('name','Channel',220,85),('group','Group',135,60),('health','Status',110,60),('url','Stream URL',420,110),('epg','EPG ID',120,55),('format','Format',85,50)]:app.table.heading(key,text=label);app.table.column(key,width=width,minwidth=minimum,stretch=True)"),
("details","details=ttk.Frame(app.panes,padding=12,width=430,style='Card.TFrame');app.panes.add(details,weight=1)","details=ttk.Frame(app.panes,padding=12,width=500,style='Card.TFrame');app.panes.add(details,weight=2)")
])

patch("studio_extras.py",[
("pil","from pathlib import Path\n","from pathlib import Path\ntry:\n    from PIL import Image, ImageTk\nexcept ImportError:\n    Image=ImageTk=None\n"),
("preview_height","self.video=tk.Frame(self,bg='#03060c',height=280 if compact else 320","self.video=tk.Frame(self,bg='#03060c',height=360 if compact else 400"),
("placeholder","self.placeholder=tk.Label(self.video,text='▶\\nPLAYLIST STUDIO',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23));self.placeholder.place(relx=.5,rely=.5,anchor='center')",
"""self.preview_source=None;self.preview_image=None
        preview_path=Path(getattr(sys,'_MEIPASS',Path(__file__).parent))/'bdix_preview.png'
        if Image is not None and preview_path.exists():
            try:self.preview_source=Image.open(preview_path).convert('RGB')
            except Exception:self.preview_source=None
        self.placeholder=tk.Label(self.video,text='BDIX-IPTV\\nPLAYLIST STUDIO 3.0',bg='#03060c',fg=ACCENT,font=('Segoe UI Semibold',23))
        self.placeholder.place(relx=.5,rely=.5,anchor='center');self.show_preview()"""),
("resize_bind","self.video.bind('<Configure>',lambda e:self.update_view())","self.video.bind('<Configure>',lambda e:(self.update_preview(),self.update_view()))"),
("preview_methods","    def start_worker(self):",
"""    def update_preview(self):
        if self.closed or self.preview_source is None:return
        try:
            w=max(320,self.video.winfo_width());h=max(180,self.video.winfo_height())
            im=self.preview_source.copy();im.thumbnail((w,h),Image.Resampling.LANCZOS)
            self.preview_image=ImageTk.PhotoImage(im);self.placeholder.configure(image=self.preview_image,text='');self.placeholder.place(relx=.5,rely=.5,anchor='center')
        except Exception:pass
    def show_preview(self):
        if self.closed:return
        self.placeholder.place(relx=.5,rely=.5,anchor='center');self.update_preview()
    def start_worker(self):"""),
("stop","def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False","def stop(self):self.commands.put(('stop',None));self.note.configure(text='Stopped.');self.paused=False;self.state=5;self.show_preview()"),
("fatal","if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False","if item[0]=='fatal':self.note.configure(text=item[1]);self.started=False;self.show_preview()"),
("error","elif item[0]=='error':self.note.configure(text=item[2])","elif item[0]=='error':self.note.configure(text=item[2]);self.show_preview()"),
("end","self.media_length=length\n","self.media_length=length\n                    if self.state in (5,6,7):self.show_preview()\n")
])

print("Feature patch complete")
