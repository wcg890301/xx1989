# 姓名名单数据
string = "哈利·波特、罗恩·韦斯莱、赫敏·格兰杰、乔治·韦斯莱、弗雷·韦斯莱、纳威、卢娜、阿不思·珀西瓦尔·邓布立多"
last_name_set = set([])
# 筛选出姓氏并打印出来
data = string.split('、')
for  name in data:
    list = name.split("·")
    if len(list) >=2:
        last_name = list[-1]
        last_name_set.add(last_name)
print(last_name_set)

data = string.split('、')
for name in data:
    list = name.split("·")
    if len(list) >= 2:
        last_name =list[-1]
        last_name_set.add(last_name)