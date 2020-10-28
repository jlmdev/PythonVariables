# Variables.py
# Recreating variables C# assignment in python

from datetime import date


def main():
    # Create variables for numberOfCupsOfCoffee, fullName, and today
    numberOfCupsOfCoffee = 3
    fullName = "Josh Mann"
    today = date.today()

    # Print the variables to the terminal
    print(fullName + " had " + str(numberOfCupsOfCoffee) +
          " cups of coffee today: " + str(today))

    # Ask the user for their name and store it in a variable named userName
    userName = input("What's your name: ")
    # Print out a greeting to the user, using their name
    print("Hi, " + userName + "!")

    # Ask the user to input 2 numbers
    # Get the numbers as strings, store them in variables named firstNumberAsString and secondNumberAsString
    firstNumberAsString = input("Enter a number: ")
    secondNumberAsString = input("Enter another number: ")

    # Convert string input to numbers
    # Convert each string to a "Double"? (Need to see if this is doable in Python)
    # store numeric values as firstOperand and secondOperand
    firstOperand = float(firstNumberAsString)
    secondOperand = float(secondNumberAsString)

    # Doing math
    # add the operands and save result as sum
    sum = firstOperand + secondOperand
    print("The sum of " + str(firstOperand) + " + " +
          str(secondOperand) + " equals: " + str(sum))
    # subtract the secondOperand from firstOperand and save the result as difference
    difference = firstOperand - secondOperand
    print("The difference of " + str(firstOperand) + " - " +
          str(secondOperand) + " equals: " + str(difference))
    # Multiply the operands and save result as product
    product = firstOperand * secondOperand
    print("The product of " + str(firstOperand) + " * " +
          str(secondOperand) + " equals: " + str(product))
    # Divide the firstOperand by the secondOperand and save result as quotient
    quotient = firstOperand / secondOperand
    print("The quotient of " + str(firstOperand) + " \u00f7 " +
          str(secondOperand) + " equals: " + str(quotient))
    # find the remainder of the operands and save the result as remainder
    remainder = firstOperand % secondOperand
    print("The remainder of " + str(firstOperand) + " \u00f7 " +
          str(secondOperand) + " equals: " + str(remainder))
    # print the values above in a meaningful way to the user


if __name__ == "__main__":
    main()
