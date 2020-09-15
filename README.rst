Ska Sphinx Theme(s)
-----------------------

This is the repository for the default Ska project documentation
theme. This theme is base on astropy-sphinx-theme. To use this theme,
simply install this package then add the following line to your
documentation's ``conf.py`` file:

.. code:: python

    html_theme = 'bootstrap-ska'

This requires Sphinx 1.6 or later to work properly. For older versions
of Sphinx, you will need to do:

.. code:: python

    import ska_sphinx_theme
    html_theme_path = ska_sphinx_theme.get_html_theme_path()
    html_theme = 'bootstrap-ska'

``bootstrap-ska`` is the only theme that is currently available, but
the structure of the package allows more themes to be added in future if
needed.

Several options for the theme can be set in the ``conf.py`` file:

.. code:: python

  html_theme_options = {
      'logotext1': 'packagename',  # white,  semi-bold
      'logotext2': '',  # orange, light
      'logotext3': ':docs',   # white,  light
      }

The ``logotext?`` options can be used to customize the top left logo.

