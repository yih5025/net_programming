import requests
import json

# 전송할 데이터를 딕셔너리 형태로 구성
data = {
    "key1": "value1",
    "key2": "value2"
}

# 데이터를 JSON 형식으로 변환
json_data = json.dumps(data)

# POST 요청으로 데이터 전송
url = "http://1.228.201.87:8010"
response = requests.post(url, json=json_data)

# 응답 확인
if response.status_code == 200:
    print("데이터 전송 성공")
else:
    print("데이터 전송 실패")