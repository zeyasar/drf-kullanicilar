import requests 
from pprint import pprint

# {'key': '37238e94d83c17b8512c23ba083ffeb209257bca'}


def client():
    token = 'Token 9b61a9c20c9e3612955764083d155e73299f4c5e'
    
    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url= 'http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers = headers,
    )
    print(response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()