import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
# import soup

key ='N0I81fzSUhrdaHT6x98p7II9uCAaJcGDpBInQTLv5ZzQV4%2FfUmQBuV27%2FDY3IHV6Agv%2BTGUazNTKqA7hMtsBOg%3D%3D'
# url = 'http://apis.data.go.kr/1611000/AptListService/getLegaldongAptList?bjdCodejdCode=%s&ServiceKey=%s' %(areacode, key)

area = pd.read_csv('data/areacode_seoul.csv', encoding = 'cp949')
kaptcode = []
kaptname = []
for i in range(len(area)):
    areacode = area['법정동코드'][i]
    req = urllib.request.Request('http://apis.data.go.kr/1611000/AptListService/getLegaldongAptList?bjdCode=%s&ServiceKey=%s' % (areacode, key))
    try:
        handler = urllib.request.urlopen(req)
        soup = BeautifulSoup(handler, "html.parser")
    except HTTPError:
        pass
    except URLError:
        pass

    if soup.totalcount.string == '0':
        pass
    else:
        kaptname.append(soup.kaptname.string)
        kaptcode.append(soup.kaptcode.string)
        print(soup.kaptname.string)
        print(soup.kaptcode.string)

code_name = pd.read_csv('C:/Users/PIRL/Desktop/code_name.csv', encoding='cp949')

code_name['code'] = kaptcode
code_name['name'] = kaptname

code_name.to_csv('C:/Users/PIRL/Desktop/code_name_result.csv', encoding='cp949')