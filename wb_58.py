from bs4 import BeautifulSoup
import  requests
import  time # 调用库

def get_item_info(url):
   # url = 'http://zhuanzhuan.58.com/detail/999275393175617542z.shtml?fullCate=5%2C46&fullLocal=845&from=pc&metric=null&PGTID=0d30002e-0034-db7b-a31d-043683686a59&ClickID=2'

    wb_data = requests.get(url) #请求目标网页并加入
    soup = BeautifulSoup(wb_data.text,'lxml') #解析网页的内容
    title_list = soup.select('h1.info_titile')
    title = title_list[0].text #取出[]标记位置的文本
    price_list = soup.select('span.price_now > i')
    price = price_list[0].text
    views_list = soup.select('span.look_time')
    views = views_list[0].text
    area_list = soup.select('div.palce_li > span > i')
    area = area_list[0].text
    cate_list = soup.select('span.crb_i > a')
    cate = cate_list[-1].text.strip()#将空格和换行删除,[-1]表示最后一个



    data = {
        'title' : title,
        'view'  : views,
        'price' : price,
        'area'  : area,
        'cate'  : cate
    }
    print(data)

def get_all_items_info():
    url = 'http://nn.58.com/wenti/?key=%E9%92%A2%E7%90%B4&cmcskey=%E9%92%A2%E7%90%B4&jump=3&searchtype=1&sourcetype=5'
    wb_data = requests.get(url)#请求URL中的内容
    soup = BeautifulSoup(wb_data.text,'lxml') #上面三步是所有网页爬取的开始基础
    hrefs_list = soup.select('a.t')
    for href in hrefs_list:
        link = href.get('href')
        if 'zhuanzhuan' in link:
            get_item_info(link)

get_all_items_info()
