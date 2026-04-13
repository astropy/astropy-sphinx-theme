"""Astropy Sphinx Theme"""

from pathlib import Path

from pydata_sphinx_theme import utils


def get_html_theme_path():
    return Path(__file__).resolve().parent / "astropy-unified"


def update_config(app) -> None:
    # Here we default some config options (i.e. things in conf.py) unless they are set by the user
    # Theme options are defaulted in theme.toml

    if not utils.config_provided_by_user(app, "html_logo"):
        app.config.html_logo = str(
            get_html_theme_path() / "static" / "img" / "astropy_logo_notext.svg"
        )

    if not utils.config_provided_by_user(app, "html_favicon"):
        app.config.html_favicon = str(get_html_theme_path() / "static" / "img" / "favicon.ico")


def setup(app):
    app.add_html_theme("astropy-unified", get_html_theme_path())
    app.add_css_file("css/astropy.css", priority=650)
    app.connect("builder-inited", update_config, priority=200)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
