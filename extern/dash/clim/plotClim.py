import numpy as np
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool

from extern.dash.dt import dtmaker

# Parameters
# EVLAND: Evaporation Land, EVPTRNS: Evapotranspiration Energy Flux, 
# WS2M: Wind Speed at 2 Meters, T2M: Temperature at 2 meters
# TS: Earth Skin Temperature, QV2M: Specific Humidity at 2 Meters, RH2M: Relative Humidity at 2 Meters
# PS: Surface Pressure, WD2M: Wind Direction at 2 Meters, CLOUD_AMT_DAY: Cloud Amount at Daylight, 
# PW: Precipitable Water, T2MDEW: The dew/frost point temperature at 2 meters above the surface of the earth
# FROST_DAYS: Frost Days, PRECTOTCORR: Precipitation Corrected

def plotESTempLastNDays(key: str, days: int = 30):
    dtClimLastWeekInterest = dtmaker.getLastNDays(key, days)[[
        "TS", "QV2M", "PS", "WD2M"
    ]]
    source = ColumnDataSource(data={
        'date': dtClimLastWeekInterest.index,
        'TS': dtClimLastWeekInterest['TS']
    })
    p = figure(x_axis_type='datetime', sizing_mode='stretch_both')
    p.height = 70
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.xaxis.major_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_line_color = "#323036"
    p.yaxis.axis_line_color = "#323036"
    p.xaxis.axis_line_width = 1.5
    p.yaxis.axis_line_width = 1.5
    p.yaxis.major_label_text_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.line('date', 'TS', source=source, line_width=2, color="#6c5ce6")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@TS")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotSHumLastNDays(key: str, days: int = 30):
    dtClimLastWeekInterest = dtmaker.getLastNDays(key, days)[[
        "TS", "QV2M", "PS", "WD2M"
    ]]
    source = ColumnDataSource(data={
        'date': dtClimLastWeekInterest.index,
        'QV2M': dtClimLastWeekInterest['QV2M']
    })
    p = figure(x_axis_type='datetime', sizing_mode='stretch_both')
    p.height = 70
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.xaxis.major_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_line_color = "#323036"
    p.yaxis.axis_line_color = "#323036"
    p.xaxis.axis_line_width = 1.5
    p.yaxis.axis_line_width = 1.5
    p.yaxis.major_label_text_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.line('date', 'QV2M', source=source, line_width=2, color="#0984e1")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@QV2M")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotSPresLastNDays(key: str, days: int = 30):
    dtClimLastWeekInterest = dtmaker.getLastNDays(key, days)[[
        "TS", "QV2M", "PS", "WD2M"
    ]]
    source = ColumnDataSource(data={
        'date': dtClimLastWeekInterest.index,
        'PS': dtClimLastWeekInterest['PS']
    })
    p = figure(x_axis_type='datetime', sizing_mode='stretch_both')
    p.height = 70
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.xaxis.major_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_line_color = "#323036"
    p.yaxis.axis_line_color = "#323036"
    p.xaxis.axis_line_width = 1.5
    p.yaxis.axis_line_width = 1.5
    p.yaxis.major_label_text_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.line('date', 'PS', source=source, line_width=2, color="#d62e2e")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@PS")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotWDirLastNDays(key: str, days: int = 30):
    dtClimLastWeekInterest = dtmaker.getLastNDays(key, days)[[
        "TS", "QV2M", "PS", "WD2M"
    ]]
    source = ColumnDataSource(data={
        'date': dtClimLastWeekInterest.index,
        'WD2M': dtClimLastWeekInterest['WD2M']
    })
    p = figure(x_axis_type='datetime', sizing_mode='stretch_both')
    p.height = 70
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.xaxis.major_tick_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.xaxis.axis_line_color = "#323036"
    p.yaxis.axis_line_color = "#323036"
    p.xaxis.axis_line_width = 1.5
    p.yaxis.axis_line_width = 1.5
    p.yaxis.major_label_text_color = None
    p.yaxis.major_tick_line_color = None
    p.yaxis.minor_tick_line_color = None
    p.line('date', 'WD2M', source=source, line_width=2, color="#e17256")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@WD2M")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

    




