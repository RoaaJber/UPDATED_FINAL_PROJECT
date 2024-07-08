# calculator.py

import sys
import requests

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y

if __name__ == "__main__":
    calc = Calculator()

 # Prompt user for entring the operation that he/she wants:
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    # Prompt user for intering values of x and y:
    try:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for x and y.")
        exit(1)

    # Perform operation based on user input
    if operation == "add":
        result = calc.add(x, y)
    elif operation == "subtract":
        result = calc.subtract(x, y)
    elif operation == "multiply":
        result = calc.multiply(x, y)
    elif operation == "divide":
        try:
            result = calc.divide(x, y)
        except ValueError as e:
            print(e)
            exit(1)
    else:
        print("Invalid operation. Please choose add, subtract, multiply, or divide.")
        exit(1)

    print(f"Result of {operation} {x} and {y} is: {result}")

    # Send result to the API endpoint in test.py
    base_url = "http://api.math.tools/"
    endpoint = base_url + "send_result"
    payload = {
        "operation": operation,
        "x": x,
        "y": y,
        "result": result
    }

    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        print("Result sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending result: {e}")
        exit(1)
        

