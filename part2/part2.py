import json
import plotly.express as px
import pandas as pd
from datetime import datetime

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    celcius = (temp_in_farenheit - 32) * 0.5556
    return celcius

with open("data/forecast_5days_a.json") as data_file:
    data = json.load(data_file)

date = []
min_temp = []
max_temp = []
real_feel_min = []
real_feel_shade_min = []

for items in data["DailyForecasts"]:
    date.append(convert_date(items["Date"]))
    min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
    max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
    real_feel_min.append(convert_f_to_c(items["RealFeelTemperature"]["Minimum"]["Value"]))
    real_feel_shade_min.append(convert_f_to_c(items["RealFeelTemperatureShade"]["Minimum"]["Value"]))
    
data = {
    "Date" : date,
    "Minimum Temperature" : min_temp,
    "Maximum Temperature" : max_temp,
    "Real Feel Minimum" : real_feel_min,
    "Real Feel Shade Minimum" : real_feel_shade_min,
}

var_1 = ["Minimum Temperature", "Maximum Temperature"]

fig_1 = px.line(data,
x="Date", 
y=var_1,
labels={"variable" : "Legend"},
title=f"Minimum and Maximum Temperature Forecast for {date[0]} to {date[-1]}"
)
fig_1.update_yaxes(title_text="Temperature in Celcius")
fig_1.show()

var_2 = ["Minimum Temperature", "Real Feel Minimum", "Real Feel Shade Minimum"]

fig_2 = px.line(data,
x="Date",
y=var_2,
labels={"variable" : "Legend"},
title=f"Actual Minimum, Real Feel Minimum, and Real Feel Shade Minimum Forecast for {date[0]} to {date[-1]}"
)
fig_2.update_yaxes(title_text="Temperature in Celcius")

fig_2.show()


