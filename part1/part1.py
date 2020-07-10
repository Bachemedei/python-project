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
    total = round(total)
    mean = total/num_items
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
    overall_min = ""
    overall_max = ""
    forecast_length = "0"

    for items in data["DailyForecasts"]:
        dates.append(convert_date(items["Date"]))
        min_temps.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        max_temps.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))

    
    print(dates)
    print(min_temps)
    print(max_temps)

    # min_total = sum(min_temperatures)
    # min_length = len(min_temperatures)
    # min_mean = format_temperature(calculate_mean(min_total, min_length))
    # lowest_min = format_temperature(min(min_temperatures))
    
    # max_total = sum(max_temperatures)
    # max_length = len(max_temperatures)
    # max_mean = format_temperature(calculate_mean(max_total, max_length))
    # highest_max = format_temperature(max(max_temperatures))


    # for items in data["DailyForecasts"]:
    #     if items["Temperature"]["Minimum"]["Value"] == min(min_temperatures):
    #         coldest_day = items["Date"]
    #     if items["Temperature"]["Maximum"]["Value"] == max(max_temperatures):
    #         hottest_day = items["Date"]

    # print("5 Day Overview")
    # print(f"    The lowest temperature will be {lowest_min}, and will occur on {coldest_day}.")
    # print(f"    The highest temperature will be {highest_max}, and will occur on {hottest_day}.")
    # print(f"    The average low this week is {min_mean}.")
    # print(f"    The average high this week is {max_mean}.")
    # print()
    
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


