from importlib.metadata import PackageNotFoundError, version

from hozan.core.app import Hozan

try:
    __version__ = version("hozan")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "Hozan",
    "__version__",
]