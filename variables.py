# Variables.py
# Recreating variables C# assignment in python
# test change
from datetime import date


def main():
    numberOfCupsOfCoffee = 3
    print("cups of coffee: " + str(numberOfCupsOfCoffee))
    fullName = "Josh Mann"
    print(fullName)
    today = date.today()
    print(today)
    print(fullName + " had " + str(numberOfCupsOfCoffee) +
          " cups of coffee today: " + str(today))


if __name__ == "__main__":
    main()
