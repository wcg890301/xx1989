import os
path = 'D:\徐歆\重要文件'
files = os.listdir(path)
for f in files:
    if f.endswith('.doc') and '徐歆' in f:
        print(f)