import numpy as np
import pandas as pd

from extern.dash.dt import dtmaker

# Parameters
# GWETPROF: Profile Soil Moisture, GWETROOT: Root Zone Soil Wetness
# GWETTOP: Surface Soil Wetness, Z0M: Surface Roughness

def calcSoilMeans(key: str, days: int = 30):
    dtSoil = dtmaker.transform(key)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    lastDays = dtSoil.iloc[-180-int(days):-180].mean().values
    lastDaysBefore = dtSoil.iloc[-(int(days)+1):-1].mean().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcSoilStd(key: str, days: int = 30):
    dtSoil = dtmaker.transform(key)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    lastDays = dtSoil.iloc[-180-int(days):-180].std().values
    lastDaysBefore = dtSoil.iloc[-(int(days)+1):-1].std().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcSoilMin(key: str, days: int = 30):
    dtSoil = dtmaker.transform(key)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    lastDays = dtSoil.iloc[-180-int(days):-180].min().values
    lastDaysBefore = dtSoil.iloc[-(int(days)+1):-1].min().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def calcSoilMax(key: str, days: int = 30):
    dtSoil = dtmaker.transform(key)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    lastDays = dtSoil.iloc[-180-int(days):-180].max().values
    lastDaysBefore = dtSoil.iloc[-(int(days)+1):-1].max().values
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), result

def getLastBeforeLast(key: str):
    dtSoil = dtmaker.transform(key)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    lastDays = dtSoil.iloc[-180].values
    lastDaysBefore = dtSoil.iloc[-181].values
    rate = np.where(lastDaysBefore != 0, 
                100 * (lastDays - lastDaysBefore) / lastDaysBefore, 
                lastDays - lastDaysBefore)
    result = ['greater' if lastDaysVal > lastDaysBeforeVal else 'equal' if lastDaysVal == lastDaysBeforeVal else 'lesser'
              for lastDaysVal, lastDaysBeforeVal in zip(lastDays, lastDaysBefore)]
    return np.round(lastDays, 2), np.round(rate, 2), result
    






