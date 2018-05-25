import requests
from bs4 import BeautifulSoup
from itertools import count


def pelicana_store():

    pList=[]
    for page in count():
    # for page in count
        url = 'http://www.pelicana.co.kr/store/stroe_search.html?page=%s'%page
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table',{'class':'table mt20'})      #태그 명,속성명:속성 값
        table_tbody = table.find('tbody')
        tr_tags=table_tbody.find_all('tr')
        for tr_tag in tr_tags:
            storeData = list(tr_tag.strings)
            name = storeData[1]
            tel = storeData[5].strip()
            address = storeData[3]

            pList.append([name,tel,address])

    return pList

result = pelicana_store()
print(result)
