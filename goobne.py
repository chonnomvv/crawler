import time
from itertools import count
import pandas as ps
from bs4 import BeautifulSoup
from selenium import webdriver


def goobneStore():
    goobneStoreList = []
    wd = webdriver.Chrome('/Users/JS-K/Documents/webdriver/Chromedriver')
    wd.get('http://goobne.co.kr/store/search_store.jsp')

    for page in count(start=48):
        wd.execute_script('store.getList(%s)' % page)
        time.sleep(0.3)
        html = wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tbody_tag = soup.find('tbody', {'id': 'store_list'})
        tr_tags = tbody_tag.find_all('tr')

        if tr_tags[0].get('class') is None:
            break

        for tr_tag in tr_tags:

            stringList = list(tr_tag.strings)
            name = stringList[1]
            tel = stringList[3]
            add = stringList[5] if stringList[3] ==' ' else stringList[6]

            goobneStoreList.append([name, tel, add])

    table = ps.DataFrame(goobneStoreList, columns=['name', 'tel', 'add'])
    table.to_csv('/Users/JS-K/Documents/json/goobneStoreList.csv', encoding='utf-8-sig', mode='w', index=True)
    return goobneStoreList

result = goobneStore()
print(result)
