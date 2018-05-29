list = [22, 23, 20, 19, 21, 22, 22, 23, 24, 20, 20, 22]
def check_in(list):
    count = 0
    for day in list:
        if day < 20:
            count = count+1

    if count != 0:
        print('有'+str(count)+'个月考情不合格。')
    else:
        print('全年合格')
check_in(list)