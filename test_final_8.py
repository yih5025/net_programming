import re
import requests

url = "https://labs.sch.ac.kr/department/iot/01.php#department-professorS"

# URL에서 페이지 내용을 가져옴
response = requests.get(url)
html_content = response.text

# 이메일 주소를 추출하는 정규 표현식 패턴
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# 정규 표현식을 사용하여 이메일 주소 추출
email_addresses = re.findall(email_pattern, html_content)

# 추출된 이메일 주소 출력
for email in email_addresses:
    print(email)
