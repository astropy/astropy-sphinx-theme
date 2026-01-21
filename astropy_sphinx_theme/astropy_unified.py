"""Astropy Sphinx Theme"""

from pathlib import Path


def setup(app):
    app.add_html_theme(
        "astropy-unified",
        Path(__file__).resolve().parent / "astropy-unified",
    )

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
