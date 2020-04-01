import uuid
from bs4 import BeautifulSoup
import requests

# Global Variables #
login_page = "http://codeforces.com/enter"


def get_csrf(request):
    page = BeautifulSoup(request.text, 'html.parser')
    csrf = page.find("input", {'name': 'csrf_token'})
    return csrf['value']


def gen_ftaa():
    return uuid.uuid4().hex.upper()[0:18]


def gen_bfaa():
    return "f1b3f18c715565b589b7823cda7448ce"


def login():
    with requests.Session() as s:
        username = input("Codeforces username: ")
        password = input("Codeforces password: ")
        request = s.get(login_page)
        params = {
            'csrf_token': get_csrf(request),
            'action': 'enter',
            'ftaa': gen_ftaa(),
            'bfaa': gen_bfaa(),
            'handleOrEmail': username,
            'password': password,
            '_tta': 90,
            'remember': 'on'
        }
        s.post(login_page, data=params)
        return s


if __name__ == "__main__":
    login()
