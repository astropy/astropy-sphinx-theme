## Astropy Sphinx Theme

This is the repository for the default Astopy project documentation theme. To use this theme, simply install this package then add the following line to your documentation's ``conf.py`` file:

```python
html_theme = 'bootstrap-astropy'
```

This requires Sphinx 1.6 or later to work properly. For older versions of Sphinx, you will need to do:

```python
import astropy_sphinx_theme
html_theme_path = astropy_sphinx_theme.get_html_theme_path()
html_theme = 'bootstrap-astropy'
```
