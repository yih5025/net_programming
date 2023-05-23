from urllib import parse

url = 'https://home.sch.ac.kr/sch/06/090000.jsp?mode=view&article_no=20220421103054 467019&board_wrapper=%2Fsch%2F06%2F090000.jsp&pager.offset=0&board_no=2020030213205 7325672'

parsed_url = parse.urlsplit(url)
print(parsed_url)
parsed_url2 = parse.urlparse(url)
print(parsed_url2)