from setuptools import setup, find_packages

from astropy_sphinx_theme import __version__

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="astropy-sphinx-theme",
    version=__version__,
    url="https://github.com/astropy/astropy-sphinx-theme",
    use_2to3=False,
    description="The sphinx theme for Astropy and affiliated packages.",
    long_description=LONG_DESCRIPTION,
    author="The Astropy Developers",
    author_email="astropy.team@gmail.com",
    install_requires=["setuptools"],
    packages=['astropy_sphinx_theme'],
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'bootstrap-astropy = astropy_sphinx_theme',
        ]
    })
