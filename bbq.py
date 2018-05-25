from itertools import count
from bs4 import BeautifulSoup
import requests
import pandas as ps

#ajax-->url을 알아내야함


bbqStoreList = []
def bbqstore():

    for page in count(start=1): #range(1,145):
        count_store = 0
        url= 'http://changup.bbq.co.kr/findstore/findstore_list.asp?page=%s'%page

        html = requests.get(url).text  #생 url 주소가 옴
        soup = BeautifulSoup(html,'html.parser')
        tbody_tag = soup.find('tbody')
        tr_tags = tbody_tag.find_all('tr')

        if len(tr_tags)<=1:
            break

        for i,tr_tag in enumerate(tr_tags):
            if i != 0:
                count_store +=1
                stringList = list(tr_tag.strings)

                name = stringList[1]
                tel = stringList[3]
                add = stringList[5]
                bbqStoreList.append([name,tel,add])

    table = ps.DataFrame(bbqStoreList, columns=['name','tel','add'])
    table.to_csv('/Users/JS-K/Documents/json/bbq_table.csv',encoding='utf-8-sig',mode='w',index=True)

    return bbqStoreList

print(bbqstore())


