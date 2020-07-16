import json
import plotly.express as px
import pandas as pd
import json
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
    "MinimumTemp" : min_temp,
    "MaxTemp" : max_temp,
    "RealFeelMin" : real_feel_min,
    "RealFeelShadeMin" : real_feel_shade_min,
}
print(data)

fig_1 = px.line(data,
x="Date", 
y=["MinimumTemp", "MaxTemp"],
labels={"variable" : "Legend"},
title=f"Minimum and Maximum Temperature Forecast for {date[0]} to {date[-1]}"
)
fig_1.update_yaxes(title_text="Temperature in Celcius")
fig_1.show()

stuff =["MinimumTemp", "RealFeelMin", "RealFeelShadeMin"]
fig_2 = px.line(data,
x="Date",
y=stuff,
labels={
    "variable" : "Legend",
    "MinimumTemp" : "Minimum Temperature in Celcius",
    "RealFeelMin" : "Real Feel Minimum Temperature in Celcius",
    "RealFeelShadeMin" : "Real Feel Shade Minimum Temperature in Celcius"
},
title=f"Actual Minimum, Real Feel Minimum, and Real Feel Shade Minimum Forecast for {date[0]} to {date[-1]}"

)
fig_2.update_yaxes(title_text="Temperature in Celcius")

fig_2.show()
