import requests, json
REST_API_KEY = '53c17c9a078fdc9512b2f1fde8468fa4'
# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post( 
        'https://api.kakaobrain.com/v1/inference/kogpt/generation', 
        json = {
        'prompt': prompt, 'max_tokens': max_tokens, 'temperature': temperature, 'top_p': top_p,
        'n': n },
    headers = {
        'Authorization': 'KakaoAK ' + REST_API_KEY
    } 
)
# 응답 JSON 형식으로 변환
    response = json.loads(r.content) 
    return response
# KoGPT에게 전달할 명령어 구성 
prompt = '''사물인터넷의 정의'''
# 파라미터를 전달해 kogpt_api()메서드 호출 
response = kogpt_api(
prompt = prompt, max_tokens = 100, temperature = 0.5, top_p = 0.5, n=3
) 
print(response)