import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.sensical.net/controlpanel'
username = input("Enter Username: ")
password = input("Enter Password" )

s = requests.Session()

data = {'un':username, 'pw':password}

r = s.post(f'{BASE_URL}/login',data=data)

soup = BeautifulSoup(r.text, 'html.parser')

if soup.select_one("a[href*=timeclocklanding.servlet]") is not None:
    print('Success!')
else:
    print('Nope')

print(r.text)
