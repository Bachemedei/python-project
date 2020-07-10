# import json
# import plotly.express as px
import json
from datetime import datetime

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    celcius = (temp_in_farenheit - 32) * 0.5556
    return celcius

with open("data/forecast_5days_a.json") as data_file:
    data = json.load(data_file)

date = []
min_temp = []
real_feel_min = []
real_feel_shade_min = []
max_temp = []


for items in data["DailyForecasts"]:
        date.append(convert_date(items["Date"]))
        min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        real_feel_min.append(convert_f_to_c(items["RealFeelTemperature"]["Minimum"]["Value"]))
        real_feel_shade_min.append(convert_f_to_c(items["RealFeelTemperatureShade"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
        items["Temperature"]["Maximum"]["Value"] = max_temp

print(date)
print(min_temp)
print(real_feel_min)
print(real_feel_shade_min)
print(max_temp)

# fig1 = px.line(data,
# x=data["DailyForecast"]["Date"], 
# y=) 
# )
