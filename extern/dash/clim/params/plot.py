# plot.py
# Plots on parameters

import numpy as np
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from scipy.stats import linregress

from extern.dash.dt import dtmaker
from extern.dash.clim.params import stat as s

def plotStyle(x_axis_type: str = "datetime"):
    p = figure(x_axis_type=x_axis_type, sizing_mode='stretch_both')
    p.height = 300
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
    return p


def plot(key: str, param: str, startYear: str, endYear:str,
        groupBy: str, plotType: str,
        color: str, trendLineColor: str = "#1a181b"):
    if endYear == "20241231":
        dt = dtmaker.transform(key)[[param]].loc[startYear:].dropna(subset=[param])
    else:
        dt = dtmaker.transform(key)[[param]].loc[startYear:endYear].dropna(subset=[param])

    if groupBy == "default":
        pass
    elif groupBy == "MY":
        dt["Month"] = dt.index.month
        vals = dt.groupby("Month")[param].mean().values
        months = np.arange(1, 13)
        textMonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        source = ColumnDataSource(data={
            'Month': months,
            'month': textMonths,
            param: vals
        })
        p = plotStyle("linear")
        p.xaxis.ticker = months
        p.vbar('Month', top=param, source=source, width=0.5, line_width=1.5, color=color)
        hover = HoverTool()
        hover.tooltips = [
            ("Month", "@month"),
            (param.capitalize(), f"@{param}")
        ]
        p.add_tools(hover)
        return p
    else:
        dt = dt.resample(groupBy).mean()
    
    dates = np.array(dt.index)
    values = dt[param].values
    
    x_numeric = np.arange(len(dates))
    slope, intercept, _, _, _ = linregress(x_numeric, values)
    trend = slope * x_numeric + intercept  # y = mx + b

    source = ColumnDataSource(data={
        'date': dt.index,
        param: dt[param],
        'trend': trend
    })
    p = plotStyle()
    
    if plotType == "line":
        p.line('date', param, source=source, line_width=1.5, color=color)
    else:
        p.circle('date', param, source=source, size=3, color=color, alpha=0.8)

    p.line('date', 'trend', source=source, line_width=3, color=trendLineColor)
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        (param, f"@{param}"),
        ("Trend", "@trend")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p

def fcstPlot(key: str, param: str, period: int, fColor: str, sColorLow: str, sColorUp: str):
    dt = s.foreCast(key, param, period)
    source = ColumnDataSource(data={
        'date': dt["ds"],
        param: dt["yhat"],
        "lower": dt["yhat_lower"],
        "upper": dt["yhat_upper"]
    })
    p = plotStyle()
    p.line('date', param, source=source, line_width=1.5, color=fColor)
    p.line('date', "lower", source=source, line_width=1.5, color=sColorLow)
    p.line('date', "upper", source=source, line_width=1.5, color=sColorUp)
    hover = HoverTool()
    hover.tooltips = [
        ("Date", "@date{%F}"),
        (param, f"@{param}"),
        ("Lower", "@lower"),
        ("Upper", "@upper")
    ]
    hover.formatters = {
        '@date': 'datetime'
    }
    p.add_tools(hover)
    return p








