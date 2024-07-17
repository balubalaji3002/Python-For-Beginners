# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:07:33 2016

@author: ericgrimson
"""

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')



# creating a calculator in python using switch statements and function

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter choice (+, -, *, /): ")

    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if operation == '+':
            print(f"The result is: {add(num1, num2)}")
        elif operation == '-':
            print(f"The result is: {subtract(num1, num2)}")
        elif operation == '*':
            print(f"The result is: {multiply(num1, num2)}")
        elif operation == '/':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()


