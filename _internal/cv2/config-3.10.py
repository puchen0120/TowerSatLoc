"""Relocatable OpenCV loader paths for the PyInstaller onedir bundle."""

import os


_loader_dir = os.path.dirname(os.path.abspath(__file__))
_bundle_root = os.path.dirname(_loader_dir)

BINARIES_PATHS = [_bundle_root] + BINARIES_PATHS
PYTHON_EXTENSIONS_PATHS = [
    os.path.join(_loader_dir, "python-3.10")
] + PYTHON_EXTENSIONS_PATHS
