#!/usr/bin/env python3
#coding = utf-8
import math
a = 90
def change():
    a = 100  # 一旦出现赋值 没有关键字global就默认为局部变量 若先打印全局变量又赋值局部变量则报错
    print(a)
def change1():
    global a # 确认用全局变量
    a = 99

def default_num(a, b, c=0, d=[]): #含默认值的参数只能放在最后
    d.append(a) ##  可变类型作为默认值 后面调用会被累加
    print('a =', a, 'b = ', b, 'c =', c)
def limitparamname(*, a = 'hhhh'):
    print(a)

def codeexplain():
    '''
    说明
    说明
    '''
    return 'hhh'

# 高阶函数
def singleExec(y):
    #print(x)
    #return [i + 6 for i in x]
    for i in y:
        print(i)
        print(type(i))
    return [ i + 6 for i in y]

def allExec(single, y):
    return single(y)

def high(l):
    return [i.upper() for i in l]
def test(h, l):
    return h(l)


def exp(x = 5):
    return x + 5
if __name__ == '__main__':
    print(a)
    change()
    print(a)
    change1()
    print(a)
    default_num(1, 2, 3)
    default_num(1, 2, 3)
    default_num(c=1, a=2, b=3) ## 可通过参数名=？形式调用 无关顺序
    limitparamname(a='hhhhsss')
    print(codeexplain())
    print(codeexplain.__doc__)
    #print(map(exp(), a))
    a = [1, 2, 3, 4, 5]
    print(list(map(exp, a)))
    print(a)    
    #print(singleExec(1))
    a = [1, 2, 8]
    print(allExec(singleExec,a))
    h = ['I', 'am', 'form', 'China']
    print(test(high, h))
    a = input('input the value of a')
    print(a)

