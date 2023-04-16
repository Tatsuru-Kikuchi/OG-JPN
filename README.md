[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3916/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3108/)
![example event parameter](https://github.com/EAPD-DRB/OG-ZAF/actions/workflows/check_black.yml/badge.svg?branch=main)

# OG-JPN

OG-JPN is an overlapping-generations (OG) model core theory, logic, and solution method algorithms that allow for dynamic general equilibrium analysis of fiscal policy. OG-JPN provides a general framework and is a dependency of several country-specific OG models, such as [OG-USA](https://github.com/PSLmodels/OG-USA) and [OG-UK](https://github.com/PSLmodels/OG-UK). The model output includes changes in macroeconomic aggregates (GDP, investment, consumption), wages, interest rates, and the stream of tax revenues over time. Regularly updated documentation of the model theory--its output, and solution method--and the Python API is available [here](https://github.com/Tatsuru-Kikuchi/OG-JPN).


## Disclaimer

The model is constantly under development, and model components could change significantly. The package will have released versions, which will be checked against existing code prior to release. Stay tuned for an upcoming release!


## Using/contributing to OG-JPN

There is only one method available for installing and running OG-JPN on your computer locally. The method is to fork and clone the most recent version of OG-JPN from its GitHub repository and create the conda environment for the `ogjpn` package. We detail both of these methods below.

### Installing and Running OG-JPN from GitHub repository

* Install the [Anaconda distribution](https://www.anaconda.com/distribution/) of Python
* Clone this repository to a directory on your computer
* From the terminal (or Conda command prompt), navigate to the directory to which you cloned this repository and run `conda env create -f environment.yml`
* Then, `conda activate ogjpn-dev`
* Then install by `pip install -e .`
* Navigate to `./examples`
* Run the model with an example reform from terminal/command prompt by typing `python run_ogjpn_example.py`
* You can adjust the `./examples/run_ogjpn_example.py` script by modifying model parameters specified in the `og_spec` dictionary.
* Model outputs will be saved in the following files:
  * `./examples/run_example_plots`
    * This folder will contain a number of plots generated from OG-JPN to help you visualize the output from your run
  * `./examples/ogjpn_example_output.csv`
    * This is a summary of the percentage changes in macro variables over the first ten years and in the steady-state.
  * `./examples/OUTPUT_BASELINE/model_params.pkl`
    * Model parameters used in the baseline run
    * See `execute.py` for items in the dictionary object in this pickle file
  * `./examples/OUTPUT_BASELINE/SS/SS_vars.pkl`
    * Outputs from the model steady state solution under the baseline policy
    * See `SS.py` for what is in the dictionary object in this pickle file
  * `./examples/OUTPUT_BASELINE/TPI/TPI_vars.pkl`
    * Outputs from the model timepath solution under the baseline policy
    * See `TPI.py` for what is in the dictionary object in this pickle file
  * An analogous set of files in the `./examples/OUTPUT_REFORM` directory, which represent objects from the simulation of the reform policy

Note that, depending on your machine, a full model run (solving for the full time path equilibrium for the baseline and reform policies) can take more than two hours of compute time.

If you run into errors running the example script, please open a new issue in the OG-JPN repo with a description of the issue and any relevant tracebacks you receive.

The CSV output file `./examples/ogjpn_example_output.csv` can be compared to the `./examples/expected_ogjpn_example_output.csv` file that is checked into the repository to confirm that you are generating the expected output. The easiest way to do this is to use the `sh example-diffs` command (or `example-diffs` on Windows) from the `examples` directory. If you run into errors running the example script, please open a new issue in the OG-JPN repo with a description of the issue and any relevant tracebacks you receive.

## Citing OG-JPN

OG-JPN (Version #.#.#)[Source code], https://github.com/Tatsuru-Kikuchi/OG-JPN
