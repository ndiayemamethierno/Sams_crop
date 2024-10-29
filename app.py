from flask import Flask, request, render_template, redirect, url_for, jsonify
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


from extern import fetch as f
from extern.dash.clim import statClim as stc
from extern.dash.clim import plotClim as ptc
from extern.dash.clim.params import stat as s
from extern.dash.clim.params import plot as p

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/home', methods=['GET','POST'])
def loadDashHome():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)

    f.coords[0] = lat
    f.coords[1] = lon
    data = f.getCachedData(lat, lon)
    if data:
        pass
    else:
        data = f.getPointData(lat, lon)
    
    f.dtDict.clear()
    f.dtDict["data"] = data
    return render_template('dashboard/home.html',rlon = lon, rlat = lat, lon=round(float(lon), 2), lat=round(float(lat), 2))

@app.route(f'/dashboard/climate', methods=['GET','POST'])
def loadDashClimate():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        cOneDays = request.args.get('cOneDays', default=30)

    means, cmpMeans = stc.calcClimMeans(key=key, days=cOneDays)
    stds, cmpStds = stc.calcClimStd(key=key, days=cOneDays)
    mins, cmpMins = stc.calcClimMin(key=key, days=cOneDays)
    maxs, cmpMaxs = stc.calcClimMax(key=key, days=cOneDays)
    current, rate, cmp = stc.getLastBeforeLast(key=key)
    pESTemp = ptc.plotESTempLastNDays(key=key, days=cOneDays)
    pSHum = ptc.plotSHumLastNDays(key=key, days=cOneDays)
    pSPres = ptc.plotSPresLastNDays(key=key, days=cOneDays)
    pWDir = ptc.plotWDirLastNDays(key=key, days=cOneDays)
    scriptESTemp, divESTemp = components(pESTemp)
    scriptSHum, divSHum = components(pSHum)
    scriptSPres, divSPres = components(pSPres)
    scriptWDir, divWDir = components(pWDir)
    return render_template('dashboard/climate.html', 
                           rlon = lon, 
                           rlat = lat,
                           mEvland = means[0],
                           mEvptrns = means[1],
                           mWs2m = means[2],
                           mT2m = means[3],
                           mTs = means[4],
                           mQv2m = means[5],
                           mRh2m = means[6],
                           mPs = means[7],
                           mWd2m = means[8],
                           mCloudAmtDay = means[9],
                           mPw = means[10],
                           mT2mDew = means[11],
                           mForstDays = means[12],
                           mPrectotCorr = means[13],
                           stdEvland = stds[0],
                           stdEvptrns = stds[1],
                           stdWs2m = stds[2],
                           stdT2m = stds[3],
                           stdTs = stds[4],
                           stdQv2m = stds[5],
                           stdRh2m = stds[6],
                           stdPs = stds[7],
                           stdWd2m = stds[8],
                           stdCloudAmtDay = stds[9],
                           stdPw = stds[10],
                           stdT2mDew = stds[11],
                           stdForstDays = stds[12],
                           stdPrectotCorr = stds[13],
                           minEvland = mins[0],
                           minEvptrns = mins[1],
                           minWs2m = mins[2],
                           minT2m = mins[3],
                           minTs = mins[4],
                           minQv2m = mins[5],
                           minRh2m = mins[6],
                           minPs = mins[7],
                           minWd2m = mins[8],
                           minCloudAmtDay = mins[9],
                           minPw = mins[10],
                           minT2mDew = mins[11],
                           minForstDays = mins[12],
                           minPrectotCorr = mins[13],
                           maxEvland = maxs[0],
                           maxEvptrns = maxs[1],
                           maxWs2m = maxs[2],
                           maxT2m = maxs[3],
                           maxTs = maxs[4],
                           maxQv2m = maxs[5],
                           maxRh2m = maxs[6],
                           maxPs = maxs[7],
                           maxWd2m = maxs[8],
                           maxCloudAmtDay = maxs[9],
                           maxPw = maxs[10],
                           maxT2mDew = maxs[11],
                           maxForstDays = maxs[12],
                           maxPrectotCorr = maxs[13],

                           cmpMeanEvland = cmpMeans[0],
                           cmpMeanEvptrns = cmpMeans[1],
                           cmpMeanWs2m = cmpMeans[2],
                           cmpMeanT2m = cmpMeans[3],
                           cmpMeanTs = cmpMeans[4],
                           cmpMeanQv2m = cmpMeans[5],
                           cmpMeanRh2m = cmpMeans[6],
                           cmpMeanPs = cmpMeans[7],
                           cmpMeanWd2m = cmpMeans[8],
                           cmpMeanCloudAmtDay = cmpMeans[9],
                           cmpMeanPw = cmpMeans[10],
                           cmpMeanT2mDew = cmpMeans[11],
                           cmpMeanForstDays = cmpMeans[12],
                           cmpMeanPrectotCorr = cmpMeans[13],
                           cmpStdEvland = cmpStds[0],
                           cmpStdEvptrns = cmpStds[1],
                           cmpStdWs2m = cmpStds[2],
                           cmpStdT2m = cmpStds[3],
                           cmpStdTs = cmpStds[4],
                           cmpStdQv2m = cmpStds[5],
                           cmpStdRh2m = cmpStds[6],
                           cmpStdPs = cmpStds[7],
                           cmpStdWd2m = cmpStds[8],
                           cmpStdCloudAmtDay = cmpStds[9],
                           cmpStdPw = cmpStds[10],
                           cmpStdT2mDew = cmpStds[11],
                           cmpStdForstDays = cmpStds[12],
                           cmpStdPrectotCorr = cmpStds[13],
                           cmpMinEvland = cmpMins[0],
                           cmpMinEvptrns = cmpMins[1],
                           cmpMinWs2m = cmpMins[2],
                           cmpMinT2m = cmpMins[3],
                           cmpMinTs = cmpMins[4],
                           cmpMinQv2m = cmpMins[5],
                           cmpMinRh2m = cmpMins[6],
                           cmpMinPs = cmpMins[7],
                           cmpMinWd2m = cmpMins[8],
                           cmpMinCloudAmtDay = cmpMins[9],
                           cmpMinPw = cmpMins[10],
                           cmpMinT2mDew = cmpMins[11],
                           cmpMinForstDays = cmpMins[12],
                           cmpMinPrectotCorr = cmpMins[13],
                           cmpMaxEvland = cmpMaxs[0],
                           cmpMaxEvptrns = cmpMaxs[1],
                           cmpMaxWs2m = cmpMaxs[2],
                           cmpMaxT2m = cmpMaxs[3],
                           cmpMaxTs = cmpMaxs[4],
                           cmpMaxQv2m = cmpMaxs[5],
                           cmpMaxRh2m = cmpMaxs[6],
                           cmpMaxPs = cmpMaxs[7],
                           cmpMaxWd2m = cmpMaxs[8],
                           cmpMaxCloudAmtDay = cmpMaxs[9],
                           cmpMaxPw = cmpMaxs[10],
                           cmpMaxT2mDew = cmpMaxs[11],
                           cmpMaxForstDays = cmpMaxs[12],
                           cmpMaxPrectotCorr = cmpMaxs[13],

                           temp = current[3],
                           rHumidity = current[6],
                           precipCorr = current[13],
                           windSpeed = current[2],
                           tempRate = rate[3],
                           rHumidityRate = rate[6],
                           precipCorrRate = rate[13],
                           windSpeedRate = rate[2],
                           tempCmp = cmp[3],
                           rHumidityCmp = cmp[6],
                           precipCorrCmp = cmp[13],
                           windSpeedCmp = cmp[2],

                           scriptESTemp=scriptESTemp,
                           divESTemp=divESTemp,
                           scriptWDir=scriptWDir,
                           divWDir=divWDir,
                           scriptSPres=scriptSPres,
                           divSPres=divSPres,
                           scriptSHum=scriptSHum,
                           divSHum=divSHum
                        )

@app.route('/dashboard/climate/evland', methods=['GET','POST'])
def loadDashClimateEvland():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="EVLAND")
    min, minDate = s.calcMin(key=key, param="EVLAND")
    max, maxDate = s.calcMax(key=key, param="EVLAND")
    plot = p.plot(key=key, param="EVLAND", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="EVLAND", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="EVLAND", period=int(fcstDays))
    return render_template('dashboard/climate/evland.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )

@app.route('/dashboard/climate/evptrns', methods=['GET','POST'])
def loadDashClimateEvptrns():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="EVPTRNS")
    min, minDate = s.calcMin(key=key, param="EVPTRNS")
    max, maxDate = s.calcMax(key=key, param="EVPTRNS")
    plot = p.plot(key=key, param="EVPTRNS", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="EVPTRNS", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="EVPTRNS", period=int(fcstDays))
    return render_template('dashboard/climate/evptrns.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )


@app.route('/dashboard/climate/ws2m', methods=['GET','POST'])
def loadDashClimateWs2m():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="WS2M")
    min, minDate = s.calcMin(key=key, param="WS2M")
    max, maxDate = s.calcMax(key=key, param="WS2M")
    plot = p.plot(key=key, param="WS2M", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="WS2M", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="WS2M", period=int(fcstDays))
    return render_template('dashboard/climate/ws2m.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )

@app.route('/dashboard/climate/t2m', methods=['GET','POST'])
def loadDashClimateT2m():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="T2M")
    min, minDate = s.calcMin(key=key, param="T2M")
    max, maxDate = s.calcMax(key=key, param="T2M")
    plot = p.plot(key=key, param="T2M", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="T2M", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="T2M", period=int(fcstDays))
    return render_template('dashboard/climate/t2m.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )

@app.route('/dashboard/climate/ts', methods=['GET','POST'])
def loadDashClimateTs():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="TS")
    min, minDate = s.calcMin(key=key, param="TS")
    max, maxDate = s.calcMax(key=key, param="TS")
    plot = p.plot(key=key, param="TS", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="TS", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="TS", period=int(fcstDays))
    return render_template('dashboard/climate/ts.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )

@app.route('/dashboard/climate/qv2m', methods=['GET','POST'])
def loadDashClimateQv2m():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="QV2M")
    min, minDate = s.calcMin(key=key, param="QV2M")
    max, maxDate = s.calcMax(key=key, param="QV2M")
    plot = p.plot(key=key, param="QV2M", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="QV2M", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="QV2M", period=int(fcstDays))
    return render_template('dashboard/climate/qv2m.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )

@app.route('/dashboard/climate/rh2m', methods=['GET','POST'])
def loadDashClimateRh2m():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        startYear = request.args.get('startYear', default=1995)
        endYear = request.args.get('endYear', default=2024)
        groupBy = request.args.get('groupBy', default="default")
        plotType = request.args.get('plotType', default="scatter")
        fcstDays = request.args.get('fcstDays', default="90")

    avg = s.calcMean(key=key, param="RH2M")
    min, minDate = s.calcMin(key=key, param="RH2M")
    max, maxDate = s.calcMax(key=key, param="RH2M")
    plot = p.plot(key=key, param="RH2M", 
                  startYear=f"{startYear}0101", endYear=f"{endYear}1231", 
                  groupBy=groupBy, plotType=plotType,
                  color="#e17256")
    fcstPlot = p.fcstPlot(key=key, param="RH2M", period=int(fcstDays),
                        fColor="#533d8f", sColorLow="#00b893", sColorUp="#d62e2e")
    script, div = components(plot)
    scriptFcst, divFcst = components(fcstPlot)
    table = s.showFcstTable(key=key, param="RH2M", period=int(fcstDays))
    return render_template('dashboard/climate/rh2m.html',
                           rlat = lat,
                           rlon = lon,
                           avg = avg[0],
                           min = min,
                           max = max,
                           minDate = minDate,
                           maxDate = maxDate,
                           script = script,
                           div = div,
                           scriptFcst = scriptFcst,
                           divFcst = divFcst,
                           fcstDays = fcstDays,
                           table = table
                        )


@app.route('/dashboard/agri/parea', methods=['GET','POST'])
def loadDashAgriPhysicalArea():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)
        year = request.args.get('year', default=None)
        tech = request.args.get('tech', default=None)
        crop = request.args.get('crop', default=None)

    data = s.getCropsData(lat, lon, "physicalArea", tech, year, crop)
    if isinstance(data, pd.DataFrame):
        crops = data.to_dict(orient='records')
    else:
        crops = data

    return render_template('dashboard/agri/parea.html',
                           rlat = lat,
                           rlon = lon, 
                           crops = crops
                        )



@app.route('/dashboard/agri/map', methods=['GET','POST'])
def loadDashMapArea():
    if request.method == 'POST':
        lon = request.form['lon']
        lat = request.form['lat']
    else:
        lon = request.args.get('lon', default=None)
        lat = request.args.get('lat', default=None)
        key = request.args.get('key', default=None)

    #nCentroid = f.getNearestCentroid(float(lat), float(lon))
    #unit = s.getAgriDataUnit(lat, lon, key="harvested/A/spam2010V2r0_global_H_TA.csv")

    return render_template('dashboard/agri/map.html',
                           rlat = lat,
                           rlon = lon
                        )

if __name__ == '__main__':
    app.run(debug=True)