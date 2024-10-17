import sys  # Importing the sys module to use system-specific parameters and functions
import time  # Importing the time module to use time-related functions

# ANSI escape sequences for coloring text
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Reset the color back to default

# Print a welcome message in cyan
print(CYAN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)

timeToSleep = 2 #variable to set the time library to 2 seconds when called
time.sleep(timeToSleep)  #Calling the time to sleep library with the variable timeToSleeps value

# Initialize variables
x = 0  # Counter to keep track of the number of loops
ellipsis = 0  # Counter to keep track of the number of dots to display

# Start a loop that will run until x reaches 20
while x != 20:
    x += 1  # Increment x by 1 with each loop iteration

    # Create a booting message in magenta, with dynamic number of dots
    message = (MAGENTA + "Infotech Center System Booting" + "." * ellipsis + RESET)

    ellipsis += 1  # Increment the number of dots in the message

    # Overwrite the current line in the terminal with the updated message
    sys.stdout.write("\r" + message)
    sys.stdout.flush()  # Ensure the message is displayed immediately

    # Wait for 0.5 seconds before proceeding to the next loop iteration
    time.sleep(1)

    # Reset ellipsis to 0 when it reaches 4, so the dots repeat from 0 to 3
    if ellipsis == 4:
        ellipsis = 0

    # After 20 iterations, print the final message in cyan and exit the loop
    if x == 20:
        print(CYAN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted" + RESET)

print("\n**************************************************************\n")

print("Weather Branch")

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


