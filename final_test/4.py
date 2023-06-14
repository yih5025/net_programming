import re
import requests

url = "https://en.wikipedia.org/wiki/Internet_of_things"


rsp = requests.get(url)
html = rsp.text
result = re.findall(r'iot+\b[A-Za-z0-9._%+-]', html)
print(result)