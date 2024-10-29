# stat.py
# Statistics on parameters

import numpy as np
import pandas as pd
from prophet import Prophet

from extern.dash.dt import dtmaker

models = {}


def calcMean(key: str, param: str):
    dt = dtmaker.transform(key)[[param]]
    lastDays = dt.mean().values
    return np.round(lastDays, 2)

def calcMin(key: str, param: str):
    dt = dtmaker.transform(key)[[param]]
    min = dt[param].min()
    date = dt[dt[param] == min].index[0]
    return min, date

def calcMax(key: str, param: str):
    dt = dtmaker.transform(key)[[param]]
    max = dt[param].max()
    date = dt[dt[param] == max].index[0]
    return max, date

def foreCast(key: str, param: str, period: int):
    dt = dtmaker.transform(key)[[param]].dropna(subset=[param])
    dt['ds'] = dt.index
    dt.rename(columns={param: 'y'}, inplace=True)
    model = models.get(f"model_{param}")
    if model is None:
        model = Prophet()
        model.fit(dt)
        models[f"model_{param}"] = model
    
    future = model.make_future_dataframe(periods=period, freq="d")
    fcst = model.predict(future)
    fcst = fcst[fcst['ds'] > dt['ds'].max()]
    return fcst

def showFcstTable(key: str, param: str, period: int):
    fcst = foreCast(key=key, param=param, period=period)
    fcst.rename(columns={'ds': 'Date', 'trend': 'Trend', 'yhat': param, 
                        'yhat_lower': 'Lower', 'yhat_upper': 'Upper'}, inplace=True)
    html = fcst[['Date', param, 'Lower', 'Upper', 'Trend']].round(2).to_html(index=False, escape=False)
    return html

def getCropsData(lat: float, lon: float, var: str, tech: str, year: str, crops: str):
    crops = [f"{crop.lower()}_{tech.lower()}" for crop in crops.split(",")] if crops else []
    dt = dtmaker.getCountryData(lat, lon, var, tech, year)
    dt.columns = dt.columns.str.lower()
    return dt[['x', 'y'] + crops]



