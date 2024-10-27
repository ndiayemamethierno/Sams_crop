import requests
import json
import pandas as pd
from pyproj import Transformer
from pymongo import MongoClient
import asyncio
import aiohttp
import time

param = ['EVLAND', 'EVPTRNS', 'GWETPROF', 'WS2M', 'WS10M', 'T2M', 'T2MWET', 'TS', 'QV2M', 'RH2M', 'PRECTOTCORR', 'PS',
    'WD2M', 'WD10M', 'CLOUD_AMT_DAY', 'PW', 'SLP']

params = ','.join(param[:])

client = MongoClient('mongodb://127.0.0.1:27017/mongosh?directConnection=true&serverSelectionTimeoutMS=2000')
db = client['sams']
fetch = db['sams_nasapower']

url = 'https://power.larc.nasa.gov/api/temporal/daily/point?parameters={}&community=RE&longitude={}&latitude={}&start=20080101&end=20231231&format=JSON'

print('Opening and transforming Pixel Data...')
df = pd.read_stata('./pixel.dta')
transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)
df['lon'], df['lat'] = transformer.transform(df['Longitude'].values, df['Latitude'].values)
coords = df[['lon', 'lat']].values
print('Successfully transformed coordinates...')

start = time.time()

def get_tasks(session):
    tasks = []
    for coord in coords[:50]:
        tasks.append(asyncio.create_task(session.get(url.format(params, coord[0], coord[1]), ssl=False)))
    return tasks


async def fetcher():
    async with aiohttp.ClientSession() as s:
        tasks = get_tasks(s)
        responses = await asyncio.gather(*tasks)
        for r in responses:
            fetch.insert_one(await r.json())

asyncio.run(fetcher())

end = time.time()

print("You did it in {}".format(end-start))


