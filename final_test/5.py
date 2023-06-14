from urllib import parse

url = 'https://search.naver.com/search/naver?query=iot'
parsed_url = parse.urlparse(url)

print(parsed_url)
print('scheme :', parsed_url.scheme) 
print('netloc :', parsed_url.netloc) 
print('path :', parsed_url.path) 
print('params :', parsed_url.params) 
print('query :', parsed_url.query) 
print('fragment:', parsed_url.fragment)

newUrl = parse.urljoin('https://search.naver.com/search/naver', parsed_url.fragment)
print(newUrl)
