import requests
from bs4 import BeautifulSoup

res = requests.get('')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('')
print(data.get_text())