# Playlist Studio 5.0 — PyInstaller VLC runtime hook.
# Runs before application imports so python-vlc receives explicit bundled paths.
import os
import sys
from pathlib import Path

_bundle_root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
_vlc_root = _bundle_root / "VLC"
_vlc_lib = _vlc_root / "libvlc.dll"
_vlc_plugins = _vlc_root / "plugins"

if _vlc_root.is_dir() and _vlc_lib.is_file():
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(str(_vlc_root))
    os.environ["PYTHON_VLC_LIB_PATH"] = str(_vlc_lib)
    os.environ["PYTHON_VLC_MODULE_PATH"] = str(_vlc_plugins)
    os.environ["VLC_PLUGIN_PATH"] = str(_vlc_plugins)
    os.environ["PATH"] = str(_vlc_root) + os.pathsep + os.environ.get("PATH", "")
else:
    raise RuntimeError(f"Bundled VLC runtime is missing or incomplete: {_vlc_root}")
