import random
import string

ran1 = random.randint(1,6)
ran2 = random.randrange(start=1,stop=50,step=3)

'''
string.digits #0-9数字
string.printable # 数字
.lower 强制转小写
.upper 强制转大写
'''
list_ch = string.printable


# print(ran1)
# print(ran2)
# print(list_ch)
def GePass(nu,ty):
    '''
    :param nu: 密码位数
    :param ty: 1：纯数字；2：数字加字幕；3数字加字母加字符
    :return: 密码
    '''

    if int(ty) == 3:
        li = string.printable.replace(' ', '').replace('\r', '')
    elif int(ty) == 1:
        li = string.digits
    elif int(ty) == 2:
        li = str(string.digits) + string.ascii_letters
    # print(li)
    cho = 'y'
    while cho == 'y':
        passcode = ''
        for i in range(int(nu)):
            passcode += random.choice(li)
            # print(x)
        print(passcode)
        cho = input('是否重新生成密码，如果需要重新生成请点击‘y’，退出点击其它:').lower()
    else:
        print('请保管好您的密码:{}'.format(passcode))
    return passcode

def GePass_m(nu,ty, som):
    '''
    :param nu: 密码位数
    :param ty: 1：纯数字；2：数字加字幕；3数字加字母加字符
    :param som: 生成密码梳理
    :return: 密码
    '''

    if int(ty) == 3:
        li = string.printable.replace(' ', '').replace('\r', '')
    elif int(ty) == 1:
        li = string.digits
    elif int(ty) == 2:
        li = str(string.digits) + string.ascii_letters
    # print(li)
    cho = 1
    passcode_list = []
    while cho <= int(som):
        passcode = ''
        for i in range(int(nu)):
            passcode += random.choice(li)
            # print(passcode)
        passcode_list.append(passcode)
        cho += 1
    # print(passcode_list)
    return passcode_list


num = input('请输入你想生成密码的位数:')
type = input('请输入你想生成密码的类型，1：纯数字；2：数字加字幕；3数字加字母加字符：')
sum = input('请输入你想生成密码的个数：')
if int(sum) > 1 :
    print(GePass_m(num,type,sum))
else:
    print(GePass(num,type))