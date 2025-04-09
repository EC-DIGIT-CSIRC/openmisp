import pathlib

from .loader import Loader

Taxonomies = Loader(pathlib.Path(__file__).parent / "data" / "misp-taxonomies")

__all__ = ["Taxonomies"]
