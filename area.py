#!/usr/bin/env python3

# Created by: Feyi Akomolafe
# Created on: Sep 2020
# This program calculates the area and perimeter of a rectangle
# with radius inputted from the user


def main():
    # this function calculates area and perimeter

    # input
    length = int(input("Enter length of the square (mm): "))
    radius = length / 2

    # process
    area = length * length + 3.14 * radius**2

    # output
    print("")
    print("Area is {0} mm2.".format(area))

    print("\nDone.")


if __name__ == "__main__":
    main()
