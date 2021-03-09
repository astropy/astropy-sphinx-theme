Astropy Sphinx Theme(s)
-----------------------

This is the repository for the default Astropy project documentation
theme(s). To use this theme, simply install this package then add the
following line to your documentation's ``conf.py`` file:

.. code:: python

    html_theme = 'bootstrap-astropy'

This requires Sphinx 1.6 or later to work properly. For older versions
of Sphinx, you will need to do:

.. code:: python

    import astropy_sphinx_theme
    html_theme_path = astropy_sphinx_theme.get_html_theme_path()
    html_theme = 'bootstrap-astropy'

``bootstrap-astropy`` is the only theme that is currently available, but
the structure of the package allows more themes to be added in future if
needed.

Several options for the theme can be set in the ``conf.py`` file:

.. code:: python

  html_theme_options = {
      'logotext1': 'packagename',  # white,  semi-bold
      'logotext2': '',  # orange, light
      'logotext3': ':docs',   # white,  light
      'astropy_project_menubar': True
      }

The ``logotext?`` options can be used to customize the top left logo, while
the ``astropy_project_menubar`` option can be set to ``True`` for packages
that are managed by the project itself (this will add links to find out more
about the Astropy project, about the team, and so on).

.. image:: https://circleci.com/gh/astropy/astropy-sphinx-theme/tree/main.svg?style=svg
    :target: https://circleci.com/gh/astropy/astropy-sphinx-theme/tree/main
