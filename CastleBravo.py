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
