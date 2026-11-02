"""larder: the server package (codename; the brand comes from settings.app_name)."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("larder-server")
except PackageNotFoundError:  # running from a source tree without an install
    __version__ = "0.0.0"
