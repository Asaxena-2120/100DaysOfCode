import requests
import os
from datetime import datetime
"""
API used: https://pixe.la/
https://docs.pixe.la/entry/post-user
"""
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.environ.get('TOKEN')
USERNAME_HABIT_TRACKER = os.environ.get('USERNAME_HABIT_TRACKER')
GRAPH_ID = "graph1"

# POST request sends data to API, but we are not interested in receiving data back,
# we just want to know the status of the request


user_params = {
    "token": TOKEN,
    "username": USERNAME_HABIT_TRACKER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# we are sending json data
# To be run once, to create a user
# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

## 2. Create a graph on pixela for our user name
graph_endpoint = f"{pixela_endpoint}/{USERNAME_HABIT_TRACKER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
# to securely send our password, which is not a parameter we create a header
# Authenticating using header
headers = {
   "X-USER-TOKEN": TOKEN
}
# to be done once to create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

## Post a pixel on graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME_HABIT_TRACKER}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you run today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

## updating a post request using put
update_endpoint = f"{pixela_endpoint}/{USERNAME_HABIT_TRACKER}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

## Deleting a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME_HABIT_TRACKER}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)