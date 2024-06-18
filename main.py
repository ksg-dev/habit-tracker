import requests
from datetime import datetime

# USERNAME = ""
# TOKEN = ""
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

yesterday = datetime(year=2024, month=6, day=17)
yesterday_str = yesterday.strftime("%Y%m%d")
# print(today_str)

# data_config = {
#     "date": today_str,
#     "quantity": "5",
# }

data_config = {
    "date": yesterday_str,
    "quantity": "15",
}

# response = requests.post(url=add_data_endpoint, json=data_config, headers=headers)
# print(response.text)

# update a pixel - today_str is date you want to update
update_endpoint = f"{add_data_endpoint}/{today_str}"

updates = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=updates, headers=headers)
# print(response.text)

# delete a pixel
# endpoint same as update in this case - just change date to one you want to delete

response = requests.delete(url=update_endpoint, headers=headers)
print(response)
