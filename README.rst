Astropy Sphinx Theme(s)
-----------------------

This is the repository for the default Astopy project documentation
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

.. image:: https://circleci.com/gh/astropy/astropy-sphinx-theme/tree/master.svg?style=svg
    :target: https://circleci.com/gh/astropy/astropy-sphinx-theme/tree/master 
