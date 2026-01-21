"""Astropy Sphinx Theme"""

from pathlib import Path


# This is kept for backwards compatibility reasons (see __init__.py)
def get_html_theme_path():
    return [str(Path(__file__).resolve().parent / "bootstrap-astropy")]


def setup(app):
    app.add_html_theme(
        "bootstrap-astropy",
        Path(__file__).resolve().parent / "bootstrap-astropy",
    )
