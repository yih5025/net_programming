import requests
import json

# 데이터를 전송할 URL
url = "http://1.228.201.87:8010"

# POST 요청을 보낼 데이터

data = {'message': 'Hello, Server!'}
headers = {'Content-Type': 'application/json'}
print(data)

response = requests.post(url, data=json.dumps(data), headers=headers)

# 응답 출력
print(response.text)

try:
    # 응답 데이터를 딕셔너리로 변환
    response_data = json.loads(response.text)

    # 딕셔너리 형태로 출력
    print(response_data)
except (json.JSONDecodeError, ValueError):
    print("Error: Failed to decode response data as JSON")
