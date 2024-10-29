import numpy as np
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool

from extern.dash.dt import dtmaker

# Parameters
# GWETPROF: Profile Soil Moisture, GWETROOT: Root Zone Soil Wetness
# GWETTOP: Surface Soil Wetness, Z0M: Surface Roughness

def plotGWETPROFLastNDays(key: str, days: int = 30):
    dtSoilLastWeekInterest = dtmaker.getLastNDays(key, days, dec=180)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    source = ColumnDataSource(data={
        'date': dtSoilLastWeekInterest.index,
        'GWETPROF': dtSoilLastWeekInterest['GWETPROF']
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
    p.line('date', 'GWETPROF', source=source, line_width=2, color="#6c5ce6")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@GWETPROF")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotGWETROOTLastNDays(key: str, days: int = 30):
    dtSoilLastWeekInterest = dtmaker.getLastNDays(key, days, dec=180)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    source = ColumnDataSource(data={
        'date': dtSoilLastWeekInterest.index,
        'GWETROOT': dtSoilLastWeekInterest['GWETROOT']
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
    p.line('date', 'GWETROOT', source=source, line_width=2, color="#0984e1")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@GWETROOT")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotGWETTOPLastNDays(key: str, days: int = 30):
    dtSoilLastWeekInterest = dtmaker.getLastNDays(key, days, dec=180)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    source = ColumnDataSource(data={
        'date': dtSoilLastWeekInterest.index,
        'GWETTOP': dtSoilLastWeekInterest['GWETTOP']
    })
    p = figure(x_axis_type='datetime', sizing_mode='stretch_both')
    p.height = 140
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
    p.line('date', 'GWETTOP', source=source, line_width=2, color="#d62e2e")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@GWETTOP")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def plotZ0MLastNDays(key: str, days: int = 30):
    dtSoilLastWeekInterest = dtmaker.getLastNDays(key, days, dec=180)[[
        "GWETPROF", "GWETROOT", "GWETTOP", "Z0M"
    ]]
    source = ColumnDataSource(data={
        'date': dtSoilLastWeekInterest.index,
        'Z0M': dtSoilLastWeekInterest['Z0M']
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
    p.line('date', 'Z0M', source=source, line_width=2, color="#e17256")
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        ("Temperature", "@Z0M")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

    




