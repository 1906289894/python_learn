"""
分支结构
"""
import random


def user_login():
    count = 0
    while count < 5:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username == '123456' and password == 'hello':
            print('{}登录成功'.format(username))
            break
        else:
            print('账户或密码错误')
        count = count + 1


'''
分数机制
'''


def get_score():
    count = 5
    curr = 0
    while curr <= count:
        score = int(input('请输入分数：'))
        curr = curr + 1
        print('共有【{}】次查询机会，当前为第{}次查询'.format(count, curr))
        if score <= 60:
            print("未及格")
        elif score == 60:
            print('刚刚及格')
        elif score > 80:
            print('成绩优秀')


def roll_dice(x=2):
    print('这个数字就是：{}'.format(x))


def roll_dice1(*x):
    print('这个数字就是：{}'.format(x))


def str_print():
    print('''
        你好呀
        很高兴认识你
    ''')


'''
生成一个大小固定的随机验证码
'''


def generate_code(i=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(i):
        x = random.randint(0, last_pos)
        code = code + all_chars[x]
    print(f'随机验证码为：{code}')


if __name__ == '__main__':
    generate_code(10)