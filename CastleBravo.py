import random
from time import sleep


# Function to simulate the gas level in the tank
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)


# Function to simulate available gas stations
def gasStations():
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)


# Function to get the distance to the nearest gas station based on the gas level
def distanceToGasStation(gasLevel):
    # Define ranges for distance based on the gas level
    if gasLevel == "Low":
        return round(random.uniform(1, 25), 1)  # Low tank - closer stations
    elif gasLevel == "Quarter Tank":
        return round(random.uniform(25.1, 50), 1)  # Quarter tank - farther stations
    return None  # For other levels, distance is irrelevant


# Function to provide alerts based on the current gas level
def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()  # Get the current gas level

    # Dictionary to map gas levels to corresponding messages and actions
    messages = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": "Your gas tank is extremely low, checking GPS for the closest gas station",
        "Quarter Tank": "Your gas tank is on a quarter of a tank, checking GPS for the closest gas station",
        "Half Tank": "Your gas tank is half full, which is plenty to get to your destination.",
        "Three Quarter Tank": "Your gas tank is three-quarters full.",
        "Full Tank": "Your gas tank is full!!! Vroom Vroom"
    }

    # Print the message for the current gas level
    print(messages[gasLevelIndicator])

    # If gas level is "Low" or "Quarter Tank", find and display the nearest gas station
    if gasLevelIndicator in ["Low", "Quarter Tank"]:
        sleep(2)  # Simulate time to check GPS
        distance = distanceToGasStation(gasLevelIndicator)
        print(f"The closest gas station is {gasStations()} which is {distance} miles away.")


# Call the function to simulate the gas level alert
gasLevelAlert()
