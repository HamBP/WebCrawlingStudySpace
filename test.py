import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.shopping.naver.com/best100v2/main.nhn')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find('title')
print(data.get_text())