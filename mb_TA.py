from bs4 import BeautifulSoup
import  requests

headers = {
    'Uesr-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

url = 'https://www.tripadvisor.cn/Attractions-g294212-Activities-oa30-Beijing.html#FILTERED_LIST'

wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')


imgs = soup.select('img[height="54"]')
for i in imgs:
    print(i.get('src'))

