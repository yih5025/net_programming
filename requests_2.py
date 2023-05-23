import requests

url = 'https://httpbin.org/post'

data = {'IoT' : '2017'}

rsp = requests.post(url, data=data)

rsp = requests.post(url, json=data)

files = {'file' : open('iot.png', 'rb')}
rsp = requests.post(url, files=files)

print(rsp.text)