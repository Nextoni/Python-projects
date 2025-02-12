import requests
from datetime import datetime


USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you cycle today?"),
}

response = requests.post(url= pixel_endpoint, json= pixel_config, headers= headers)
print(response.text)


pixel_update_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_config = {
    "quantity" : "30"
}

# response = requests.put(url= pixel_update_endpoint, json= pixel_update_config, headers= headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url= delete_endpoint, headers=headers)
# print(response.text)