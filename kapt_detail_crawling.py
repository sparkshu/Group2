import pandas as pd
from matplotlib import rcParams
rcParams['font.family'] = 'NanumGothic'
import urllib
import json

con = pd.read_csv('C:/Users/PIRL/Desktop/apt_result.csv', encoding='cp949')
apt = pd.DataFrame()
value_err_list = []
type_err_list = []
key_list = ['CODE_HEAT', 'SUBWAY_STATION', 'SUBWAY_LINE', 'DISPOSAL_TYPE', 'CODE_ECON', 'KAPTD_CCCNT', 'KAPTD_ECNTM',
            'WELFARE_FACILITY', 'KAPT_BCOMPANY', 'KAPT_USEDATE', 'KAPTD_WTIMEBUS', 'KAPTD_WTIMESUB', 'CODE_HALL', 'CODE_SALE',
            'EDUCATION_FACILITY', 'KAPT_CODE']

# apt 거래 내역 정보
def readAptData( dongcode, year, quarter ) :
    url = "http://rt.molit.go.kr/rtApt.do?cmd=getTradeAptLocal&dongCode=%d&danjiCode=ALL&srhYear=%d&srhPeriod=%d&gubunRadio2=1" % ( dongcode, year, quarter )
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    apt_meta = pd.DataFrame(data['danjiList'])
    apt_data = pd.DataFrame(data['detailList'])
    return apt_meta, apt_data

for i in range(len(con)):
    try:
        code = con['KAPT_CODE'][i]
        response = urllib.request.urlopen("http://www.k-apt.go.kr/kaptinfo/getKaptInfo_detail.do?kapt_code=%s" % (code) )
        data = response.read().decode('utf-8')
        raw_data = json.loads(data)

        if len(raw_data['resultMap_kapt']) != 0:
            apt = pd.DataFrame({'CODE_HEAT': [0],
                                'SUBWAY_STATION': [0],
                                'SUBWAY_LINE': [0],
                                'DISPOSAL_TYPE': [0],
                                'CODE_ECON': [0],
                                'KAPTD_CCCNT': [0],
                                'KAPTD_ECNTM': [0],
                                'WELFARE_FACILITY': [0],
                                'KAPT_BCOMPANY': [0],
                                'KAPT_USEDATE': [0],
                                'KAPTD_WTIMEBUS': [0],
                                'KAPTD_WTIMESUB': [0],
                                'CODE_HALL': [0],
                                'CODE_SALE': [0],
                                'EDUCATION_FACILITY': [0],
                                'KAPT_CODE': [0]
                                })
            for key in key_list:
                if raw_data['resultMap_kapt'][key] != None:
                    apt[key] = raw_data.get('resultMap_kapt').get(key)

            apt.to_csv('C:/Users/PIRL/Desktop/kapt_detail_crawling_result.csv', mode='a', encoding='cp949')
            print("inserted data: ", i)
            # print(i, " is completed")
    except json.decoder.JSONDecodeError:
        print("decode error : ", i)
        break
    except ValueError:
        value_err_list.append(i)
        print("value error : ", i)
        pass
    except TypeError:
        type_err_list.append(i)
        print(type_err_list)
