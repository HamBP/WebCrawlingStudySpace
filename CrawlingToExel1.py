import os
import sys
import urllib.request
import json
import openpyxl
from bs4 import BeautifulSoup

# 크롤링
client_id = "lXW31hbm7TIjx3tMGm1I"
client_secret = "cPBMBL_xtk"
encText = urllib.parse.quote("컴퓨터 공학")
url = "https://openapi.naver.com/v1/search/blog?display=100&query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    res = response_body.decode('utf-8')
    res = json.loads(res)
else:
    print("Error Code:" + rescode)

# 데이터 저장
exel_file = openpyxl.Workbook()
sheet = exel_file.active
sheet.append(['bloggername', 'link', 'title', 'description', 'postdate'])
sheet.column_dimensions['A'].width = 30
sheet.column_dimensions['B'].width = 50
sheet.column_dimensions['C'].width = 50
sheet.column_dimensions['D'].width = 50

for i in range(100):
    insert_data = res['items'][i]

    parse_title = BeautifulSoup(insert_data['title'], 'html.parser').get_text()
    parse_des = BeautifulSoup(insert_data['description'], 'html.parser').get_text()
    sheet.append([
        insert_data['bloggername'], # 블로그 이름
        insert_data['link'], # url
        parse_title, # 제목
        parse_des, # 본문
        insert_data['postdate'] # 게시 날짜
    ])

exel_file.save('blog_search.xlsx')
exel_file.close()
