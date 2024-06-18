import requests
from datetime import datetime

USERNAME = "ksg-dev"
TOKEN = "aiuehfo82398hfalsej"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# create user
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# View Graph: https://pixe.la/v1/users/ksg-dev/graphs/graph1.html

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# add value to graph
add_data_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today_str = today.strftime("%Y%m%d")
# print(today_str)

data_config = {
    "date": today_str,
    "quantity": "5",
}

# response = requests.post(url=add_data_endpoint, json=data_config, headers=headers)
# print(response.text)
