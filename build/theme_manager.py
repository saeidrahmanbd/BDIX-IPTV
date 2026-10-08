from __future__ import annotations

import json
import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk

THEMES = {
    "Dark": {"bg":"#0b1117","panel":"#101923","surface":"#16222d","field":"#0d171f","fg":"#f1f5f9","muted":"#9fb0bf","accent":"#00d7c7","border":"#2a3b49","selected":"#123f46"},
    "Blue": {"bg":"#081521","panel":"#0d2234","surface":"#12324b","field":"#0a1c2b","fg":"#eef7ff","muted":"#a7bdd0","accent":"#1687ff","border":"#315674","selected":"#124b7e"},
    "Green": {"bg":"#07150e","panel":"#0d2619","surface":"#123c27","field":"#091c12","fg":"#effff5","muted":"#a8c5b3","accent":"#22c55e","border":"#315a43","selected":"#145b35"},
    "Purple": {"bg":"#10091a","panel":"#1b1029","surface":"#2b1844","field":"#150d21","fg":"#f8f1ff","muted":"#c0adc9","accent":"#a855f7","border":"#54346e","selected":"#4a2370"},
    "Light": {"bg":"#f3f6fa","panel":"#ffffff","surface":"#e7edf5","field":"#ffffff","fg":"#152033","muted":"#5f6f82","accent":"#1677ff","border":"#c6d2df","selected":"#dcecff"},
    "Classic": {"bg":"#e8edf3","panel":"#f7f9fb","surface":"#d9e1ea","field":"#ffffff","fg":"#1d2733","muted":"#586777","accent":"#2f6f9f","border":"#aebdcb","selected":"#c8dced"},
}

class ThemeManager:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(root)
        self.current = self._load()
        self._settings_button = None
        self._settings_command = None
        self.apply(self.current)
        root.after(250, self._install_settings_menu)
        root.after(1000, self._install_settings_menu)

    @property
    def config_path(self):
        base = Path(os.environ.get("APPDATA") or (Path.home() / ".config"))
        p = base / "Playlist Studio"
        p.mkdir(parents=True, exist_ok=True)
        return p / "theme.json"

    def _load(self):
        try:
            n = json.loads(self.config_path.read_text(encoding="utf-8")).get("theme", "Dark")
            return n if n in THEMES else "Dark"
        except Exception:
            return "Dark"

    def _save(self):
        try:
            self.config_path.write_text(json.dumps({"theme": self.current}, indent=2), encoding="utf-8")
        except Exception:
            pass

    def select(self, name):
        if name in THEMES:
            self.current = name
            self.apply(name)
            self._save()

    def _cfg(self, style, **kw):
        try:
            self.style.configure(style, **kw)
        except Exception:
            pass

    def apply(self, name):
        c = THEMES[name]
        try: self.root.configure(bg=c["bg"])
        except Exception: pass
        self._cfg("TFrame", background=c["bg"])
        self._cfg("TLabel", background=c["bg"], foreground=c["fg"])
        self._cfg("TButton", background=c["surface"], foreground=c["fg"], bordercolor=c["border"], padding=(9,5))
        self._cfg("TEntry", fieldbackground=c["field"], foreground=c["fg"], bordercolor=c["border"])
        self._cfg("TCombobox", fieldbackground=c["field"], foreground=c["fg"], background=c["surface"])
        self._cfg("Treeview", background=c["field"], fieldbackground=c["field"], foreground=c["fg"], rowheight=30)
        self._cfg("Treeview.Heading", background=c["surface"], foreground=c["fg"], bordercolor=c["border"], padding=(7,6))
        self._cfg("TNotebook", background=c["panel"], bordercolor=c["border"])
        self._cfg("TNotebook.Tab", background=c["surface"], foreground=c["fg"], padding=(12,6))
        self._cfg("TCheckbutton", background=c["bg"], foreground=c["fg"])
        self._cfg("TRadiobutton", background=c["bg"], foreground=c["fg"])
        self._cfg("TScale", background=c["bg"], troughcolor=c["surface"])
        for w in self._walk(self.root):
            try:
                if isinstance(w, ttk.Widget):
                    st = w.cget("style")
                    if st:
                        klass = w.winfo_class()
                        if "Button" in klass: self._cfg(st, background=c["surface"], foreground=c["fg"], bordercolor=c["border"])
                        elif "Label" in klass: self._cfg(st, background=c["panel"], foreground=c["fg"])
                        elif "Frame" in klass: self._cfg(st, background=c["panel"])
                        elif "Entry" in klass or "Combobox" in klass: self._cfg(st, fieldbackground=c["field"], foreground=c["fg"], background=c["field"])
                    continue
                cls = w.winfo_class()
                if cls in ("Frame","Labelframe"): w.configure(bg=c["panel"])
                elif cls == "Label": w.configure(bg=c["panel"], fg=c["fg"])
                elif cls == "Canvas": w.configure(bg=c["field"])
                elif cls in ("Entry","Spinbox","Text"): w.configure(bg=c["field"], fg=c["fg"], insertbackground=c["fg"])
                elif cls == "Listbox": w.configure(bg=c["field"], fg=c["fg"], selectbackground=c["accent"], selectforeground="#ffffff")
                elif cls == "Button": w.configure(bg=c["surface"], fg=c["fg"], activebackground=c["accent"], activeforeground="#ffffff")
            except Exception:
                pass
        try:
            self.root.option_add("*Menu.background", c["panel"])
            self.root.option_add("*Menu.foreground", c["fg"])
            self.root.option_add("*Menu.activeBackground", c["accent"])
            self.root.option_add("*Menu.activeForeground", "#ffffff")
        except Exception:
            pass

    def _walk(self, w):
        yield w
        try:
            for child in w.winfo_children():
                yield from self._walk(child)
        except Exception:
            return

    def _find_settings(self):
        for w in self._walk(self.root):
            try:
                t = str(w.cget("text")).strip().lower()
                if t == "settings" or t.startswith("settings "):
                    if isinstance(w, (tk.Button, ttk.Button, tk.Menubutton, ttk.Menubutton)):
                        return w
            except Exception:
                pass
        return None

    def _settings_popup(self, button):
        c = THEMES[self.current]
        menu = tk.Menu(button, tearoff=False, bg=c["panel"], fg=c["fg"], activebackground=c["accent"], activeforeground="#ffffff")
        sub = tk.Menu(menu, tearoff=False, bg=c["panel"], fg=c["fg"], activebackground=c["accent"], activeforeground="#ffffff")
        var = tk.StringVar(button, value=self.current)
        for name in THEMES:
            sub.add_radiobutton(label=name, variable=var, command=lambda n=name: self.select(n))
        menu.add_cascade(label="Themes", menu=sub)
        original = self._settings_command
        def general():
            if original:
                try: self.root.tk.call(original); return
                except Exception: pass
        menu.add_separator()
        menu.add_command(label="General Settings", command=general)
        menu.tk_popup(button.winfo_rootx(), button.winfo_rooty()+button.winfo_height())

    def _install_settings_menu(self):
        b = self._find_settings()
        if b is None or getattr(b, "_ps_theme_wrapped", False):
            return
        try: original = b.cget("command")
        except Exception: original = ""
        self._settings_button, self._settings_command = b, original
        try:
            b.configure(command=lambda btn=b: self._settings_popup(btn))
            b._ps_theme_wrapped = True
        except Exception:
            pass

def install_theme_support(root):
    m = getattr(root, "_playlist_studio_theme_manager", None)
    if m is None:
        m = ThemeManager(root)
        root._playlist_studio_theme_manager = m
    return m
