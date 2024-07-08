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

 # Prompt user for operation
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    # Prompt user for values of x and y
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
    base_url = "https://api.math.tools/"
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
** This class is designed to handle basic arithmetic operations for integers and floats, and it raises an error if we have tried to devide any numer over Zero, it's allwing the user to pass a value and then it will do he arthmatic and then send them to the API end point. 
=======================================================================================================================================================================++
# test.py

import requests

base_url = "https://api.math.tools/"
endpoint = base_url + "numbers/nod"

response = requests.get(endpoint)

my_num = response.json()
my_num = my_num["contents"]["nod"]["numbers"]["number"]

# This part sends a GET request to https://api.math.tools/numbers/nod to retrieve some number data (my_num).
# It extracts my_num from the JSON response (response.json()).


end_point = base_url + f"numbers/base?number={my_num}&from=10&to=16"
end_point
hexa_response = requests.get(end_point)
hexa_response.json()
# the above will convert my_num to hexadecimal (base 16)

# Now, we can retrieve the result from the calculator endpoint
calculator_endpoint = base_url + "get_result"
calculator_response = requests.get(calculator_endpoint)

if calculator_response.status_code == 200:
    calculator_result = calculator_response.json()
    print(f"Result from calculator: {calculator_result['result']}")
else:
    print(f"Failed to retrieve result from calculator: {calculator_response.status_code}")
#Explanation





