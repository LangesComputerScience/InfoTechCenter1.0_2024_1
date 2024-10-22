# Prints a formatted title for the gasoline branch program
print("\n*****************************************\n")
print("Gasoline Branch\n")

# Importing necessary libraries
import random  # Used for random selection
from time import sleep  # Used for adding delays between actions


# Function to simulate the gas level in the tank
def gasLevelGauge():
    # List representing different possible gas levels in the tank
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly choose a gas level from the list
    return random.choice(gasLevelList)


# Function to simulate available gas stations
def gasStations():
    # List of gas station names
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    # Randomly choose a gas station from the list
    return random.choice(gasStationsList)


# Function to provide alerts based on the current gas level
def gasLevelAlert():
    # Generate a random distance to a gas station when the tank is low
    milesToGasStationLow = round(random.uniform(1, 25), 1)  # Distance between 1 and 25 miles
    # Generate a random distance to a gas station when on a quarter tank
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)  # Distance between 25.1 and 50 miles

    # Get the current gas level using the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Conditional statements to check the gas level and provide appropriate alerts
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Pause for 2 seconds before the next action
        print("Calling Triple AAA")  # Suggesting the user needs roadside assistance
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        # Displays a random gas station and the distance to it
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)
        # Displays a random gas station and the distance when the tank is a quarter full
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")
    elif gasLevelIndicator == "Half Tank":
        # Half tank scenario, indicating no urgent action needed
        print("Your gas tank is a half a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        # Three-quarter tank scenario
        print("Your gas tank is three quarter tanks full.")
    else:
        # Full tank scenario
        print("Your gas tank is full!!!  Vroom Vroom")


# Call the function to simulate the gas level alert
gasLevelAlert()
