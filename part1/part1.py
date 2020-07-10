import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

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
    celcius = round(celcius, 1)
    return celcius


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total/num_items
    mean = round(mean, 1)
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as data_file:
        data = json.load(data_file)

  
    dates = []
    min_temps = []
    max_temps = []
    forecast_length = 0
    day_description = []
    day_rain = []
    night_description = []
    night_rain = []

    for items in data["DailyForecasts"]:
        date = convert_date(items["Date"])
        dates.append(date)
        minimum = (convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        min_temps.append(minimum)
        maximum = (convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
        max_temps.append(maximum)
        overall_min = min(min_temps)
        overall_max = max(max_temps)
        if minimum == overall_min:
            coldest_day = date
        if maximum == overall_max:
            hottest_day = date
        day_description.append(items["Day"]["LongPhrase"])
        day_rain.append(items["Day"]["RainProbability"])
        night_description.append(items["Night"]["LongPhrase"])
        night_rain.append(items["Night"]["RainProbability"])
        

    min_total = sum(min_temps)
    min_mean = calculate_mean(min_total, len(min_temps))
    max_total = sum(max_temps)
    max_mean = calculate_mean(max_total, len(max_temps))

    overview = f"""{len(dates)} Day Overview
    The lowest temperature will be {format_temperature(overall_min)}, and will occur on {coldest_day}.
    The highest temperature will be {format_temperature(overall_max)}, and will occur on {hottest_day}.        
    The average low this week is {format_temperature(min_mean)}.
    The average high this week is {format_temperature(max_mean)}.
    """
    
    index = 0

    while index != len(dates):
        overview = overview + f"""
-------- {dates[index]} --------
Minimum Temperature: {format_temperature(min_temps[index])}
Maximum Temperature: {format_temperature(max_temps[index])}
Daytime: {day_description[index]}
    Chance of rain:  {day_rain[index]}%
Nighttime: {night_description[index]}
    Chance of rain:  {night_rain[index]}%
    """
        index = index + 1

    return overview


    # for items in data["DailyForecasts"]:
    #     print(f"""-------- { items[Date] } --------""")
    #     Minimum Temperature: { items["Temperature"]["Minimum"]["ValueString"] }
    #     Maximum Temperature: { ["Temperature"]["Maximum"]["ValueString"] }
    #     Daytime: { items["Day"]["LongPhrase"] }
    #         Chance of rain: { str(items["Day"]["PrecipitationProbability"]) } %
    #     Nighttime: { items["Night"]["LongPhrase"] }
    #         Chance of rain: { str(items["Night"]["PrecipitationProbability"]) } %
    #     """)


        # print("--------" + items["Date"] + "--------")
        # print("Minimum Temperature: " + items["Temperature"]["Minimum"]["ValueString"])
        # print("Maximum Temperature: " + items["Temperature"]["Maximum"]["ValueString"])
        # print("Daytime: " + items["Day"]["LongPhrase"])
        # print("    Chance of rain: " + str(items["Day"]["PrecipitationProbability"]) + "%")
        # print("Nighttime: " + items["Night"]["LongPhrase"])
        # print("    Chance of rain: " + str(items["Night"]["PrecipitationProbability"]) + "%")
        # print()
   
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))


