#!/usr/bin/env python3

# Created By: Luke
# Date: Feb 28, 2025
# Calculates the circumference of a circle using tau using radius
import math
import constants

# Adds math module


def main():
    print(
        "This program will calculate the circumference of a circle using the radius and TAU."
    )
    # Intro message
    radius = float(input(("Enter the radius of your circle: ")))
    # Asks user for circumference input
    print()
    circumference = constants.TAU * radius
    # Calculates circumference
    print("The circumference is: {:.2f}".format(circumference))
    # Displays circumference


if __name__ == "__main__":
    main()
