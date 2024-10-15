# Print a header to introduce the program
print("\n**********************************\n")

# Title for the system or program being presented
print("Weather Branch\n")

# Importing necessary libraries
# 'random' is used to pick a random weather condition
# 'sleep' is used to add a delay to simulate system processing time
import random
from time import sleep


# Function to randomly choose a weather condition
def weather():
    # List of possible weather conditions
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]

    # Randomly select one weather condition from the list
    weatherCondition = random.choice(weatherForecast)

    # Return the selected weather condition
    return weatherCondition


# Call the weather function and store the result in the 'weatherAlert' variable
weatherAlert = weather()


# Function to determine the vehicle's response based on the weather alert
def vehicleResponseSystem():
    # Check if the weather is snowy
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)  # Simulate system processing delay
        print("\nVRS system has been engaged only allowing you to drive 55mph.")

    # Check if the weather is a blizzard
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 45mph.")

    # Check if the weather is rainy
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 65mph.")

    # Check if the weather is windy
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 70mph.")

    # Check if the weather is icy
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("\nVRS system has been engaged only allowing you to drive 30mph.")

    # If none of the above, it must be sunny or clear skies
    else:
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS system has been disengaged.")


# Call the vehicleResponseSystem function to execute the program logic
vehicleResponseSystem()
