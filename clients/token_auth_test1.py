import requests 
from pprint import pprint

# {'key': '37238e94d83c17b8512c23ba083ffeb209257bca'}


def client():
    credentials = {
        'username' : 'test3',
        'password' : 'z123456y'
    }

    response = requests.post(
        url= 'http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
    )
    print(response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()