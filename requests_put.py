import requests

url = 'https://httpbin.org/put'

data = {'IoT' : '2017'}
rsp  = requests.put(url, data=data)

print(rsp.text)

tsp = requests.put(url, json=data)
print(tsp.text)

files = {'file' : open('iot.png', 'rb')}
jsp = requests.put(url, files=files)
print(jsp.text)