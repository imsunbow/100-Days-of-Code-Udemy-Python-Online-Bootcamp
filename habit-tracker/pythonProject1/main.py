import requests
from datetime import datetime

USERNAME = "jaeminjaemin"
TOKEN = "fsdfqewqw"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# 사용자 생성
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 사용자 등록 (이미 등록된 경우 주석 처리)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 그래프 생성
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# 그래프 등록 (이미 생성된 경우 주석 처리)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2024,month=11,day=27)

# 픽셀 추가
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),  # YYYYMMDD 형식
    "quantity": input("How many kilometers did you cycle today?"),  # 기록 값
}

#
# print(today.strftime("%Y%m%d"))
#
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5",
}

# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
