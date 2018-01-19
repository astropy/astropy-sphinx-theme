from setuptools import setup, find_packages

from sphinx_astropy_theme import __version__

setup(
    name="sphinx-astropy-theme",
    version=__version__,
    use_2to3=False,
    description="The sphinx theme for Astropy.",
    long_description="The documentation theme for the Astropy project and affiliated packages.",
    author="The Astropy Developers",
    author_email="astropy@scipy.org",
    install_requires=[
        "setuptools",
    ],
    packages=['sphinx_astropy_theme'],
    include_package_data=True,
)
