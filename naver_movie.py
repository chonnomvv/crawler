import requests
from bs4 import BeautifulSoup

def naver_movie():
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    html = requests.get(url).text       #
    soup = BeautifulSoup(html,'html.parser')
    # 하나를 받아올 땐 .find, 여러개를 받아 올 땐 find_all
    tags = soup.find_all('div',{'class':'tit3'})     #태그가 div인 것, 속성(class)이 값(tit3인 것)
    print(type(tags))
    for index, tag in enumerate(tags):
        tag.a.text
        print(type(tag.a.text))
        print(index+1, tag.a.text)


naver_movie()