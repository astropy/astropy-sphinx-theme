from setuptools import setup, find_packages

from ska_sphinx_theme import __version__

with open("README.rst") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="ska-sphinx-theme",
    version=__version__,
    url="https://github.com/sot/ska-sphinx-theme",
    use_2to3=False,
    description="The sphinx theme for Ska packages.",
    long_description=LONG_DESCRIPTION,
    author="The Ska Developers",
    author_email="aca@cfa.harvard.edu",
    install_requires=["setuptools"],
    packages=['ska_sphinx_theme'],
    include_package_data=True,
    entry_points = {
        'sphinx.html_themes': [
            'bootstrap-ska = ska_sphinx_theme',
        ]
    })
