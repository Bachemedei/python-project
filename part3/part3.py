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

with open("data/historical_6hours.json") as data_file:
    data = json.load(data_file)

temps = []
time = []
precipitation = []
daylight_hour = []
uv_index = []
