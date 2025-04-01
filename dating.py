#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 31, 2025
# Description: Program to determine if you can date a grandchild based on age criteria.

# Constants for age boundaries
MIN_AGE = 25  # Minimum approved age
MAX_AGE = 40  # Maximum approved age

# Ask the user for their age
print("Please enter your age:")

try:
    age = int(input())  # Convert input to integer

    # Check if the age is within the approved range using logical AND
    if age > MIN_AGE and age < MAX_AGE:
        print("You can date their grandchild.")  # Output for valid age range
    else:
        print("You cannot date their grandchild.")  # Output for age outside the range
except ValueError:
    print("Invalid input, please enter a valid age.")  # Handle non-integer input

# Print the closing message
print("Thanks for playing.")  # End message for the user
