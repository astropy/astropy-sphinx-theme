import warnings

from .bootstrap_astropy import get_html_theme_path as _old_theme_path


def get_html_theme_path():
    warnings.warn(
        "astropy_sphinx_theme.get_html_theme_path is deprecated, you shouldn't"
        " need to manually specify the theme path as the theme is registered with sphinx",
        DeprecationWarning,
        stacklevel=2,
    )
    return _old_theme_path()
