import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def convert_time(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")

def convert_f_to_c(temp_in_farenheit):
    celcius = (temp_in_farenheit - 32) * 0.5556
    return celcius

def process_weather(historical_file):
    with open(historical_file) as data_file:
        data = json.load(data_file)

    date = convert_date(data[0]["LocalObservationDateTime"])
    iso_time = []
    time = []
    temps = []
    real_feel_temps = []
    precip_hours = 0
    precip_total = 0
    daylight_hours = 0
    uv_index = []
    
    index = 0

    for item in data:
        iso_time.append(item["LocalObservationDateTime"])
        time.append(convert_time(item["LocalObservationDateTime"]))
        temps.append(item["Temperature"]["Metric"]["Value"])
        real_feel_temps.append(item["RealFeelTemperature"]["Metric"]["Value"])
        if item["HasPrecipitation"] == True:
            precip_hours += 1
        precip_total += item["Precip1hr"]["Metric"]["Value"]
        if item["IsDayTime"] == True:
            daylight_hours += 1
        uv_index.append(item["UVIndex"])
        index +=1

    min_temp = min(temps)
    min_hour = time[temps.index(min(temps))]
    max_temp = max(temps)
    max_hour = time[temps.index(max(temps))]
    max_uv = max(uv_index)
    max_uv_hour = time[uv_index.index(max(uv_index))]

    output = f"""--- {len(time)} Hour Historical Weather Summary for {date} ---
    The minimum temperature of {format_temperature(min_temp)} occurred at {min_hour}.
    The maximum temperature of {format_temperature(max_temp)} occurred at {max_hour}.
    Precipitation occurred for {precip_hours} hours, totalling {precip_total}mm.
    The period occurred over {daylight_hours} hours.
    The maximum UV index of {max_uv} occurred at {max_uv_hour}.
    """  

    # with open(f"{len(time)}hour_output.txt", "w") as txt_file:
    #     txt_file.write(output)
        
    return {"temps" : temps, "real_feel_temps" : real_feel_temps, "iso_time" : iso_time, "time" : time, "date" : date}

data = process_weather("data/historical_6hours.json")
time = []


if len(data["time"]) < 24:
    title = data["time"][0] + " to "+ data["time"][-1]+ " on "+ data["date"]
else: 
    title = data["date"]


fig = go.Figure()
fig.add_trace(go.Box(y=data["temps"], name="Temperature"))
fig.add_trace(go.Box(y=data["real_feel_temps"], name="Real Feel Temperature"))
fig.update_layout(
    title=f"Hourly Actual vs Real Feel Temperatures in Celcius for {title}",
    yaxis_title="Temperature in Celcius",
    legend_title="Legend"
)

fig.show()

