[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3916/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3108/)
![example event parameter](https://github.com/EAPD-DRB/OG-ZAF/actions/workflows/check_black.yml/badge.svg?branch=main)

# OG-JPN

OG-JPN is an overlapping-generations (OG) model core theory, logic, and solution method algorithms that allow for dynamic general equilibrium analysis of fiscal policy. OG-JPN provides a general framework and is a dependency of several country-specific OG models, such as [OG-USA](https://github.com/PSLmodels/OG-USA) and [OG-UK](https://github.com/PSLmodels/OG-UK). The model output includes changes in macroeconomic aggregates (GDP, investment, consumption), wages, interest rates, and the stream of tax revenues over time. Regularly updated documentation of the model theory--its output, and solution method--and the Python API is available at [here](https://pslmodels.github.io/OG-Core).


## Disclaimer

The model is constantly under development, and model components could change significantly. The package will have released versions, which will be checked against existing code prior to release. Stay tuned for an upcoming release!


## Using/contributing to OG-JPN

There is only one method available for installing and running OG-JPN on your computer locally. The method is to fork and clone the most recent version of OG-JPN from its GitHub repository and create the conda environment for the `ogjpn` package. We detail this method below.

### Installing and Running OG-JPN from GitHub repository

* Install the [Anaconda distribution](https://www.anaconda.com/distribution/) of Python
* Clone this repository to a directory on your computer
* From the terminal (or Conda command prompt), navigate to the directory to which you cloned this repository and run `conda env create -f environment.yml`
* Then, `conda activate ogjpn-dev`
* Then install by `pip install -e .`
* Navigate to `./run_examples`
* Run the model with an example reform from terminal/command prompt by typing `python run_ogjpn_example.py`
* You can adjust the `./run_examples/run_ogjpn_example.py` script by modifying model parameters specified in the `og_spec` dictionary.
* Model outputs will be saved in the following files:
  * `./run_examples/run_example_plots`
    * This folder will contain a number of plots generated from OG-JPN to help you visualize the output from your run
  * `./run_examples/ogjpn_example_output.csv`
    * This is a summary of the percentage changes in macro variables over the first ten years and in the steady-state.
  * `./run_examples/OUTPUT_BASELINE/model_params.pkl`
    * Model parameters used in the baseline run
    * See `execute.py` for items in the dictionary object in this pickle file
  * `./run_examples/OUTPUT_BASELINE/SS/SS_vars.pkl`
    * Outputs from the model steady state solution under the baseline policy
    * See `SS.py` for what is in the dictionary object in this pickle file
  * `./run_examples/OUTPUT_BASELINE/TPI/TPI_vars.pkl`
    * Outputs from the model timepath solution under the baseline policy
    * See `TPI.py` for what is in the dictionary object in this pickle file
  * An analogous set of files in the `./run_examples/OUTPUT_REFORM` directory, which represent objects from the simulation of the reform policy

Note that, depending on your machine, a full model run (solving for the full time path equilibrium for the baseline and reform policies) can take more than two hours of compute time.

If you run into errors running the example script, please open a new issue in the OG-JPN repo with a description of the issue and any relevant tracebacks you receive.

Once the package is installed, one can adjust parameters in the OG-Core `Specifications` object using the `Calibration` class as follows:

```
from ogcore.parameters import Specifications
from ogjpn.calibrate import Calibration
p = Specifications()
c = Calibration(p)
updated_params = c.get_dict()
p.update_specifications({'initial_debt_ratio': updated_params['initial_debt_ratio']})
```

## Core Maintainers

The core maintainer of the OG-JPN repository is:

* Tatsuru Kikuchi (GitHub handle: [Tatsuru_Kikuchi](https://github.com/Tatsuru-Kikuchi)), Research Officer, Faculty of Economics, The University of Tokyo.

## Citing OG-JPN

OG-JPN (Version 1.0.0)[Source code], https://github.com/Tatsuru-Kikuchi/OG-JPN
