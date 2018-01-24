from setuptools import setup, find_packages

from astropy_sphinx_theme import __version__

setup(
    name="astropy-sphinx-theme",
    version=__version__,
    use_2to3=False,
    description="The sphinx theme for Astropy.",
    long_description="The documentation theme for the Astropy project and affiliated packages.",
    author="The Astropy Developers",
    author_email="astropy.team@gmail.com",
    install_requires=["setuptools"],
    packages=['astropy_sphinx_theme'],
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'bootstrap-astropy = astropy_sphinx_theme',
        ]
    },)
