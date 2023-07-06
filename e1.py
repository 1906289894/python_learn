import time
import random

def get_dividor(n):
    '''
    获得一个能被n整除的随机数
    '''
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)
    return random.choice(l)



if __name__ == '__main__':
    ops = ['+', '-', '*', '/']
    start_time = time.time()
    total = 0
    correct = 0
    questions = []
    while time.time() - start_time <= 60:
        a = random.randint(1, 99)
        op = random.choice(ops)
        if op == '/':
            b = get_dividor(a)
        else:
            b = random.randint(1, 99)
        # 正确答案
        a_op_b = '{}{}{}'.format(a, op, b)
        c = int(eval(a_op_b))

        #让用户输入答案
        try:
            ans = int(input('{}='.format(a_op_b)))
        except:
            ans = ''
        
        # 检查答案是否正确
        if time.time() - start_time <= 60:
            if c == ans:
                print('正确！剩余时间{}秒。'.format(int(60 - (time.time() - start_time))))
                correct = correct + 1
            else:
                print('错误！剩余时间{}秒。'.format(int(60 - (time.time() - start_time))))
            total = total + 1
            questions.append('{}={}, 正确答案：{}'.format(a_op_b, ans, c))
    print('{}道题目，正确率 {:.2f}%。'.format(total, correct / total * 100))
    for q in questions:
        print(q)   

