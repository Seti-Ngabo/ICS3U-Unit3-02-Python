#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program guesses a random number

import constants


def main():
    # this function checks if the random number is correct

    # input
    guess = int(input("Enter the number between 0 and 9: "))
    print("")

    # process and output
    if guess == constants.THE_NUMBER:
        print("Correct")
        print("\nDone.")
    else:
        print("wrong, try again.")


if __name__ == "__main__":
    main()
