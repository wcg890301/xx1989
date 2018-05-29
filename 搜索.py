import os
path = 'D:\徐歆\重要文件'
files = os.listdir(path)
# print(files)

for f in files:
    if '1' in f and f.endswith('.png'):
        print('Found it' + f)