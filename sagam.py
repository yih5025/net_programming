import requests
import json
import time

# 데이터를 전송할 URL
url = "http://1.228.201.87:8010"

# POST 요청을 보낼 데이터


data = {
    "warning" : "0",
    "room" : ''
    }
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

while True:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    # response = requests.post(url, json=data)
    


    # 응답 확인
    try:
        # 응답 데이터를 딕셔너리로 변환
        response_data = response.json()

        # 딕셔너리 형태로 출력
        print(response_data)
    except (json.JSONDecodeError, ValueError):
        print("Error: Failed to decode response data as JSON")

    time.sleep(3)
