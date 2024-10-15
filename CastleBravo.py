print("\n**************************************************************\n")

print("Welcome Branch")

import random
from time import sleep


# Function to randomly choose a weather condition
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    return random.choice(weatherForecast)


# Call the weather function to get the current weather alert
weatherAlert = weather()

# Dictionary to store weather conditions and their corresponding alarm delay and speed limit
weather_responses = {
    "snowy": {"alarm_delay": 30, "speed_limit": 55},
    "blizzard": {"alarm_delay": 45, "speed_limit": 45},
    "rainy": {"alarm_delay": 15, "speed_limit": 65},
    "windy": {"alarm_delay": 5, "speed_limit": 70},
    "icy": {"alarm_delay": 50, "speed_limit": 30}
}


# Function to determine the vehicle's response based on the weather alert
def vehicleResponseSystem():
    # Check if the current weather is in the dictionary (i.e., not "sunny")
    if weatherAlert in weather_responses:
        # Get the corresponding alarm delay and speed limit
        alarm_delay = weather_responses[weatherAlert]["alarm_delay"]
        speed_limit = weather_responses[weatherAlert]["speed_limit"]

        print(f"\nThe National Weather Service has updated our alarm by {alarm_delay} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS system has been engaged only allowing you to drive {speed_limit}mph.")
    else:
        # If it's sunny or not in the dictionary, VRS is disengaged
        print(f"\nThe NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")


# Execute the vehicle response system
vehicleResponseSystem()

