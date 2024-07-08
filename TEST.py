# test.py

import requests

base_url = "http://api.math.tools/"
endpoint = base_url + "numbers/nod"

response = requests.get(endpoint)

my_num = response.json()
my_num = my_num["contents"]["nod"]["numbers"]["number"]

end_point = base_url + f"numbers/base?number={my_num}&from=10&to=16"
end_point
hexa_response = requests.get(end_point)
hexa_response.json()

# Now, we can retrieve the result from the calculator endpoint
calculator_endpoint = base_url + "get_result"
calculator_response = requests.get(calculator_endpoint)

if calculator_response.status_code == 200:
    calculator_result = calculator_response.json()
    print(f"Result from calculator: {calculator_result['result']}")
else:
    print(f"Failed to retrieve result from calculator: {calculator_response.status_code}")
#Explanation