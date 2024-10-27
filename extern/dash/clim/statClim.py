import numpy as np
import pandas as pd

from extern.dash.dt import dtmaker

# Parameters
# EVLAND: Evaporation Land, EVPTRNS: Evapotranspiration Energy Flux, 
# WS2M: Wind Speed at 2 Meters, T2M: Temperature at 2 meters
# TS: Earth Skin Temperature, QV2M: Specific Humidity at 2 Meters, RH2M: Relative Humidity at 2 Meters
# PS: Surface Pressure, WD2M: Wind Direction at 2 Meters, CLOUD_AMT_DAY: Cloud Amount at Daylight, 
# PW: Precipitable Water, T2MDEW: The dew/frost point temperature at 2 meters above the surface of the earth
# FROST_DAYS: Frost Days, PRECTOTCORR: Precipitation Corrected

def calcClimMeans(key: str, days: int = 30):
    dtClim = dtmaker.transform(key)[[
        "EVLAND", "EVPTRNS", "WS2M", "T2M", "TS", "QV2M", "RH2M", "PS", "WD2M",
        "CLOUD_AMT_DAY", "PW", "T2MDEW", "FROST_DAYS", "PRECTOTCORR"
    ]]
    lastDays = dtClim.iloc[-int(days):].mean().values
    lastDaysBefore = dtClim.iloc[-(int(days)+1):-1].mean().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcClimStd(key: str, days: int = 30):
    dtClim = dtmaker.transform(key)[[
        "EVLAND", "EVPTRNS", "WS2M", "T2M", "TS", "QV2M", "RH2M", "PS", "WD2M",
        "CLOUD_AMT_DAY", "PW", "T2MDEW", "FROST_DAYS", "PRECTOTCORR"
    ]]
    lastDays = dtClim.iloc[-int(days):].std().values
    lastDaysBefore = dtClim.iloc[-(int(days)+1):-1].std().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcClimMin(key: str, days: int = 30):
    dtClim = dtmaker.transform(key)[[
        "EVLAND", "EVPTRNS", "WS2M", "T2M", "TS", "QV2M", "RH2M", "PS", "WD2M",
        "CLOUD_AMT_DAY", "PW", "T2MDEW", "FROST_DAYS", "PRECTOTCORR"
    ]]
    lastDays = dtClim.iloc[-int(days):].min().values
    lastDaysBefore = dtClim.iloc[-(int(days)+1):-1].min().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcClimMax(key: str, days: int = 30):
    dtClim = dtmaker.transform(key)[[
        "EVLAND", "EVPTRNS", "WS2M", "T2M", "TS", "QV2M", "RH2M", "PS", "WD2M",
        "CLOUD_AMT_DAY", "PW", "T2MDEW", "FROST_DAYS", "PRECTOTCORR"
    ]]
    lastDays = dtClim.iloc[-int(days):].max().values
    lastDaysBefore = dtClim.iloc[-(int(days)+1):-1].max().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def getLastBeforeLast(key: str):
    dtClim = dtmaker.transform(key)[[
        "EVLAND", "EVPTRNS", "WS2M", "T2M", "TS", "QV2M", "RH2M", "PS", "WD2M",
        "CLOUD_AMT_DAY", "PW", "T2MDEW", "FROST_DAYS", "PRECTOTCORR"
    ]]
    lastDays = dtClim.iloc[-7].values
    lastDaysBefore = dtClim.iloc[-8].values
    rate = np.where(lastDaysBefore != 0, 
                100 * (lastDays - lastDaysBefore) / lastDaysBefore, 
                lastDays - lastDaysBefore)
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), np.round(rate, 2), result
    






