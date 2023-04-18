"""
This module uses data from FRED to find values for parameters for the
OG-JPN model that rely on macro data for calibration.
"""
# imports
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime
import statsmodels.api as sm

CUR_PATH = os.path.split(os.path.abspath(__file__))[0]
DATA_DIR = os.path.join(CUR_PATH, "data", "macro")

def get_macro_params():
    """
    Compute values of parameters that are derived from macro data
    """
    # set beginning and end dates for data
    # format is year (1940),month (1),day (1)
    start = datetime.datetime(1970, 1, 1)
    end = datetime.datetime(2021, 3, 31)  # go through today
    baseline_date = datetime.datetime(2021, 1, 1)
    baseline_date2 = datetime.datetime(2021, 3, 31)

    variable_dict_fred = {
        "GDP Per Capita": "NYGDPPCAPKDJPN",
        "Labor share": "LABSHPJPA156NRUG",
        "Debt to GDP ratio": "GGGDTAJPA188N",
        "Outstanding Domestic Public Debt to GDP": "DDDM04JPA156NWDB",
        "BAA Corp Bond Rates": "DBAA",
        "10 year govt bond rate": "IRLTLT01JPM156N",
        "Transfers as a share of GDP": "DDOI11JPA156NWDB",
        # "Social Security payments": "W823RC1",
        "Gov expenditures": "JPNGFCEQDSMEI",
        # "Gov interest payments": "A091RC1Q027SBEA",
        "Real GDP": "JPNRGDPEXP",
        "Nominal GDP": "NGDPSAXDCJPQ",
    }

    # pull series of interest using pandas_datareader
    fred_data = web.DataReader(variable_dict_fred.values(), "fred", start, end)
    fred_data.rename(
        columns=dict((y, x) for x, y in variable_dict_fred.items()), inplace=True
    )

    # make sure all dollar value data are in billions
    # fred_data["Debt held by public"] = fred_data["Debt held by public"] / 1000

    # Separate quartely, monthly, and annual dataseries
    fred_data_q = (
        fred_data[
            [
                "Nominal GDP",
                #"Transfers as a share of GDP",
                # "Social Security payments",
                "Gov expenditures",
                # "Gov interest payments",
                "GDP Per Capita",
            ]
        ]
        .resample("Q")
        .mean()
    )
    fred_data_a = fred_data[
        ["Labor share", "Outstanding Domestic Public Debt to GDP", "Transfers as a share of GDP"]
    ]
    fred_data_d = fred_data[["BAA Corp Bond Rates", "10 year govt bond rate"]]

    # initialize a dictionary of parameters
    macro_parameters = {}

    # print(fred_data.loc(str(baseline_date)))
    # find initial_debt_ratio
    macro_parameters["initial_debt_ratio"] = (
        pd.Series(fred_data_a["Outstanding Domestic Public Debt to GDP"]).loc[
            baseline_date2
        ]
        / 100
    )

    # # find alpha_T
    macro_parameters["alpha_T"] = 
    pd.Series(fred_data_a["Transfers as a share of GDP"]).loc[baseline_date]

    # # find alpha_G
    raw_data = os.path.join(DATA_DIR, "wb_gov_cons.csv")
    df = pd.read_csv(raw_data)
    macro_parameters["alpha_G"] = df["data"].loc[baseline_date]

    # find gamma
    macro_parameters["gamma"] = [1 - fred_data_a["Labor share"].mean()]

    # find g_y
    macro_parameters["g_y_annual"] = (
        fred_data_q["GDP Per Capita"].pct_change(periods=4, freq="Q").mean()
    )

    # estimate r_gov_shift and r_gov_scale
    rate_data = fred_data_d[
        ["10 year govt bond rate", "BAA Corp Bond Rates"]
    ].dropna()
    rate_data["constant"] = np.ones(len(rate_data.index))
    # mod = PanelOLS(fred_data['10 year govt bond rate'],
    #                fred_data[['constant', 'BAA Corp Bond Rates']])
    mod = sm.OLS(
        rate_data["10 year govt bond rate"],
        rate_data[["constant", "BAA Corp Bond Rates"]],
    )
    res = mod.fit()
    macro_parameters["r_gov_shift"] = res.params["BAA Corp Bond Rates"]
    macro_parameters["r_gov_scale"] = res.params["constant"]

    return macro_parameters