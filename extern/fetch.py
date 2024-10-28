# fetch.py

# this file is the one responsible for fetching data on Power Larc NASA web site
# The principle is to get interesting parameters that can be analysed for future use purpose
# taking into account that the number of parameter per API call is limited to 20
# Thus, we will be collecting the data in several shots if necessary
# Be aware of the fact that we are using the Agroclimatology (AG) as default community for data requests

import requests
import pandas as pd
from pymongo import MongoClient
import numpy as np
from datetime import date, timedelta

param = [
    'EVLAND', # Evaporation Land: The evaporation over land at the surface of the earth
    'EVPTRNS', # Evapotranspiration Energy Flux: The evapotranspiration energy flux at the surface of the earth.
    'GWETPROF', # Profile Soil Moisture
    'WS2M', # Wind Speed at 2 Meters
    'T2M', # Temperature at 2 meters
    'TS', # Earth Skin Temperature: The average temperature at the earth's surface
    'QV2M', # Specific Humidity at 2 Meters: The ratio of the mass of water vapor to the total mass of air at 2 meters (g water/kg total air).
    'RH2M', # Relative Humidity at 2 Meters: The ratio of actual partial pressure of water vapor to the partial pressure at saturation, expressed in percent.
    'PS', # Surface Pressure
    'WD2M', # Wind Direction at 2 Meters
    'CLOUD_AMT_DAY', # Cloud Amount at Daylight
    'PW', # Precipitable Water: The total atmospheric water vapor contained in a vertical column of the atmosphere
    'T2MDEW', # The dew/frost point temperature at 2 meters above the surface of the earth
    'FROST_DAYS', # Frost Days: A frost day occurs when the 2m temperature cools to the dew point temperature and both are less than 0 C or 32 F.
    'GWETROOT', # Root Zone Soil Wetness
    'GWETTOP', # Surface Soil Wetness
    'PRECTOTCORR', # Precipitation Corrected
    'Z0M' #Surface Roughness
]

params = ','.join(param[:])
client = MongoClient('mongodb://127.0.0.1:27017/mongosh?directConnection=true&serverSelectionTimeoutMS=2000')
db = client['sams']
wsCol = db['wsCollection']

start = "19950101"
end = date.today() - timedelta(days=2)
end = end.strftime("%Y%m%d")
url = 'https://power.larc.nasa.gov/api/temporal/daily/point?parameters={}&community=RE&longitude={}&latitude={}&start={}&end={}&format=JSON&header=false'

dtDict: dict = {}
coords = [None, None]

def getPointData(lat: float, lon: float):
    r = requests.get(url.format(params, lon, lat, start, end))
    data = {
        "lat": lat,
        "lon": lon,
        "data": r.json()
    }
    wsCol.insert_one(data)
    return data

def getCachedData(lat, lon):
    data = wsCol.find_one({"lat": lat, "lon": lon})
    return data






