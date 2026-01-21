"""Astropy Sphinx Theme"""

from pathlib import Path


def setup(app):
    app.add_html_theme(
        "bootstrap-astropy",
        Path(__file__).resolve().parent / "bootstrap-astropy",
    )
