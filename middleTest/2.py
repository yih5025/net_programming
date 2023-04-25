str = 'https://search.daum.net/search?w=tot&q=bigdata'
dic = dict()

msg = str.split('?')
wmsg = msg[1].split('&')

dicmsg = wmsg[0].split('=')
icmsg = wmsg[1].split('=')


dic['w'] = 'tot'
dic['q'] = 'bigdata'

print(dic)

dic['q'] = 'iot'

print(dic)