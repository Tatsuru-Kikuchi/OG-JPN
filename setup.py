import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    longdesc = fh.read()

setuptools.setup(
    name="ogjpn",
    version="1.0.0",
    author="Tatsuru Kikuchi"
    license="CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    description="An overlapping generations model for fiscal policy analysis in Japan",
    long_description_content_type="text/markdown",
    long_description=longdesc,
    url: "https://github.com/Tatsuru-Kikuchi/OG-JPN/",
    download_url: "https://github.com/Tatsuru-Kikuchi/OG-JPN/",
    packages=["ogjpn"],
    package_data={
        "ogjpn": [
            "default_parameters.json",
        ]
    },
    iinclude_packages=True,
    python_requires=">=3.10,
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
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: CC0 1.0 Universal public domain dedication",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    "tests_require": ["pytest"],
)
