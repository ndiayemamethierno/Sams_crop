import pandas as pd
import numpy as np
from datetime import date, timedelta
import os

from extern import fetch as f

start = "19950101"
end = date.today() - timedelta(days=2)
end = end.strftime("%Y%m%d")

def getData(key: str):
    return f.dtDict[key]

def transform(key: str):
    dates = pd.date_range(start=start, end=end, freq='D')
    df = pd.DataFrame(index=dates)
    params = getData(key)["data"]["properties"]["parameter"]
    for param, values in params.items():
        param_data = pd.Series(values)
        param_data.index = pd.to_datetime(param_data.index, format='%Y%m%d')
        df[param] = param_data

    df.replace(-999, np.nan, inplace=True)
    return df

def getLastNDays(key: str, n: int = 30, dec: int = 0):
    df = transform(key)
    return df.iloc[-7-int(n)-dec:-7]

def getCountryData(lat: float, lon: float, var: str, tech: str, year: str, type: str = "country"):
    return f.getCountryData(lat, lon, var, tech, year)

# def getCountryRasterDataFromPoint(lat: float, lon: float, var: str, tech: str, year: str, crops: str):
#     return f.runFetcher(lat, lon, var, tech, year, crops)



