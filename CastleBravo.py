import sys  # Importing the sys module to use system-specific parameters and functions
import time  # Importing the time module to use time-related functions

# Print a welcome message
print("\nWelcome to InfoTechCenter V1.0\n")

# Initialize variables
x = 0  # Counter to keep track of the number of loops
ellipsis = 0  # Counter to keep track of the number of dots to display

# Start a loop that will run until x reaches 20
while x != 20:
    x += 1  # Increment x by 1 with each loop iteration

    # Create a booting message that includes a dynamic number of dots
    message = ("Infotech Center System Booting" + "." * ellipsis)

    ellipsis += 1  # Increment the number of dots in the message

    # Overwrite the current line in the terminal with the updated message
    sys.stdout.write("\r" + message)

    # Wait for 0.5 seconds before proceeding to the next loop iteration
    time.sleep(.5)

    # Reset ellipsis to 0 when it reaches 4, so the dots repeat from 0 to 3
    if ellipsis == 4:
        ellipsis = 0

    # After 20 iterations, print the final message and exit the loop
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
