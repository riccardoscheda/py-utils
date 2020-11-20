import datetime
from os.path import dirname, join

import pandas as pd
from scipy.signal import savgol_filter

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DataRange1d, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure
import numpy as np

def get_dataset(src, name):
	df = pd.read_csv('covid-plot/data/data.csv',
			  parse_dates=['Date'],
			 encoding="ISO-8859-1",
			 dtype={"RegionName": str,
			        "RegionCode": str},
			 error_bad_lines=False)
	df["DailyChangeConfirmedCases"] = df.groupby(["CountryName"]).ConfirmedCases.diff().fillna(0)
	df = df[df["CountryName"]== select.value]
	return ColumnDataSource(data=df)

def make_plot(source, title):
    plot = figure(x_axis_type="datetime", plot_width=800, tools="", toolbar_location=None)
    plot.title.text = title

    #plot.line("Date","ConfirmedCases",source=source)
    plot.line("Date","DailyChangeConfirmedCases",source=source)
    # fixed attributes

    return plot

def update_plot(attrname, old, new):
    
    plot.title.text = "Daily Cases for " + select.value

    src = get_dataset(df, df[df["CountryName"]==select.value]['ConfirmedCases'])
    source.data.update(src.data)

city = 'Italy'
	


df = pd.read_csv('covid-plot/data/data.csv',
	          parse_dates=['Date'],
			 encoding="ISO-8859-1",
			 dtype={"RegionName": str,
			        "RegionCode": str},
			 error_bad_lines=False)
options = list(np.unique(df["CountryName"]))
select = Select(value="Italy", title='Country', options=options)

source = get_dataset(df[df["CountryName"]== select.value],select.value)

select.on_change('value', update_plot)
plot = make_plot(source, "Daily Cases for " + select.value)

controls = column(select)

curdoc().add_root(row( controls,plot))
curdoc().title = "Weather"
