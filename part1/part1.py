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
    forecast_length = 0
    min_total = 0
    max_total = 0

    for items in data["DailyForecasts"]:
        date = convert_date(items["Date"])
        dates.append(date)
        minimum = (convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        min_temps.append(minimum)
        maximum = (convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
        max_temps.append(maximum)
        min_total =+ minimum
        max_total =+ maximum
        forecast_length =+ 1
        overall_min = min(min_temps)
        overall_max = max(max_temps)
        if minimum == overall_min:
            coldest_day = date
        if maximum == overall_max:
            hottest_day = date


    

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


