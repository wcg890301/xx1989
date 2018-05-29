import  random
def roll_dice(numbers=3,points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []#创建一个列表
    while numbers > 0:#循环条件
        point = random.randrange(1,7)#随机数创建
        points.append(point) #把数值添加进列表
        numbers = numbers - 1#让while停止循环的条件
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <=10 #定义大和小
    if isBig:
        return  'Big'
    elif isSmall:
        return 'Small'

def start_game():
    your_money = 1000
    while your_money > 0:#循环条件
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['Big', 'Small']  # 选择的列表
        your_choice = input('Big or Small :')  # 输入选择.
        your_bet = input("The amount you're betting on: ")#下注的金额
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are',points,'You win !')
                print('恭喜，你赢了{}元，你现在有{}元本金'.format(your_bet, your_money + int(your_bet)))
                your_money = your_money + int(your_bet)#字符串要转换INT进行计算
            else:
                print('The points are',points,'You lose !')
                print('遗憾，你输了{}元，你现在有{}元本金'.format(your_bet, your_money - int(your_bet)))
                your_money = your_money - int(your_bet)
        else:
            print('Invalid Words')
    else:
        print('Game Over!')

start_game()