import pandas as pd
from matplotlib import rcParams
rcParams['font.family'] = 'NanumGothic'
import urllib
import json


con = pd.read_csv('C:/Users/PIRL/Desktop/areacode_result.csv', encoding='cp949')
apt = pd.DataFrame()
value_err_list = []

for i in range(13955, 14000):
    try:

        code = con['법정동코드'][i]
        response = urllib.request.urlopen("http://www.k-apt.go.kr/kaptinfo/getKaptList.do?bjd_code=%s" % (code))
        data = response.read().decode('utf-8')
        raw_data = json.loads(data)

        if len(raw_data['resultList']) != 0:
            apt = pd.DataFrame({'BJD_CODE': [[0] for _ in range(len(raw_data['resultList']))],
                                'KAPT_NAME': [[0] for _ in range(len(raw_data['resultList']))],
                                'KAPT_CODE': [[0] for _ in range(len(raw_data['resultList']))],
                                'BJD_NAME': [[0] for _ in range(len(raw_data['resultList']))]})

            for j in range(len(raw_data['resultList'])):
                apt['BJD_CODE'][j] = raw_data['resultList'][j]['BJD_CODE']
                apt['KAPT_NAME'][j] = raw_data['resultList'][j]['KAPT_NAME']
                apt['KAPT_CODE'][j] = raw_data['resultList'][j]['KAPT_CODE']
                apt['BJD_NAME'][j] = raw_data['resultList'][j]['BJD_NAME']

                apt.to_csv('C:/Users/PIRL/Desktop/kapt_crawling_result_test.csv', mode='a', encoding='cp949')
            # print(i, " is completed")
    except json.decoder.JSONDecodeError:
        print("decode error : ", i)
        break
    except ValueError:
        value_err_list.append(i)
        print("value error : ", i)
        pass

