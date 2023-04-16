try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as f:
    longdesc = f.read()

version = "0.0.0"

config = {
    "description": "JPN Calibration for OG-Core",
    "long_description": longdesc,
    "url": "https://github.com/Tatsuru-Kikuchi/OG-JPN/",
    "download_url": "https://github.com/Tatsuru-Kikuchi/OG-JPN/",
    "version": version,
    "license": "CC0 1.0 Universal public domain dedication",
    "packages": ["ogjpn"],
    "include_package_data": True,
    "name": "ogjpn",
    "install_requires": [
        "numpy",
        "psutil",
        "scipy>=1.5.0",
        "pandas>=1.2.5",
        "matplotlib",
        "dask>=2.30.0",
        "distributed>=2.30.1",
        "paramtools>=0.15.0",
        "taxcalc>=3.0.0",
        "requests",
        "rpy2",
        "pandas-datareader",
        "xlwt",
        "openpyxl>=3.1.2",
        "statsmodels",
        "linearmodels",
        "ogcore",
    ],
    "package_data": {"ogjpn": ["data/PSID/*"]},
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: CC0 1.0 Universal public domain dedication",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    "tests_require": ["pytest"],
}

setup(**config)
