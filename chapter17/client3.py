import requests

def get_items(q=None, skip=0, limit=100):
    url = 'http://localhost:8000/items/'
    params = {
        'q': q,
        'skip': skip,
        'limit': limit
    }
    response = requests.get(url, params=params)
    return response.json()

# 클라이언트 함수 호출 예제
if __name__ == "__main__":
    # 'q' 파라미터에 'example'을 넣고, 기본 'skip'과 'limit' 값 사용
    result = get_items(q="example")
    print(result)
