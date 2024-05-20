import requests
from datetime import datetime

USERNAME = "wonjun"
TOKEN = "dldnjswns"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "code1",
#     "name": "coding Graph",
#     "unit": "h",
#     "type": "int",
#     "color": "ajisai",
# }
#
headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/code1"
#
today = datetime.now()

# post_pixel = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "2",
# }
#
# response = requests.post(url=pixel_endpoint, json=post_pixel, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/code1/{today.strftime("%Y%m%d")}"

put_config = {
    "quantity": "9",
}

response = requests.put(url=pixel_update_endpoint, json=put_config, headers=headers)

print(response.text)