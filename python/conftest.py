from pathlib import Path
import sys
import types


PYTHON_ROOT = Path(__file__).resolve().parent


def _iter_python_project_dirs():
    for child in PYTHON_ROOT.iterdir():
        if not child.is_dir():
            continue
        if child.name.startswith(".") or child.name == "tests":
            continue
        if any(grandchild.suffix == ".py" for grandchild in child.iterdir()):
            yield child


for project_dir in sorted(_iter_python_project_dirs()):
    sys.path.insert(0, str(project_dir))


class _DummySurface:
    def __init__(self, _size):
        self.size = _size

    def fill(self, _color):
        return None


sys.modules.setdefault("pygame", types.SimpleNamespace(Surface=_DummySurface))
