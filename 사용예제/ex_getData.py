import urllib.request

class GetData:
    key ='N0I81fzSUhrdaHT6x98p7II9uCAaJcGDpBInQTLv5ZzQV4%2FfUmQBuV27%2FDY3IHV6Agv%2BTGUazNTKqA7hMtsBOg%3D%3D'
    url = 'http://apis.data.go.kr/1611000/AptBasisInfoService/getAphusBassInfo?kaptCode=A10027875&ServiceKey=%s' %key

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        print(data.decode('utf-8'))


getData = GetData()
getData.main()