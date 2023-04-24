from setuptools import setup

DESCRIPTION = 'An overlapping generations model for fiscal policy analysis in Japan'
NAME = 'ogjpn'
AUTHOR = 'Tatsuru Kikuchi'
AUTHOR_EMAIL = 'tatsuru.kikuchi@e.u-tokyo.ac.jp'
URL = 'https://github.com/Tatsuru-Kikuchi/OG-JPN'
LICENSE = 'MIT'
DOWNLOAD_URL = URL
VERSION = '1.0.0'
python_requires=">=3.10"
INSTALL_REQUIRES = [
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
        "ogcore"
]
PACKAGES = [
    'ogjpn'
]
CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]
with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
LONG_DESCRIPTION = readme
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url=URL,
    download_url=URL,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    install_requires=INSTALL_REQUIRES
)
