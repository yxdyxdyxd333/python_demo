#! /usr/bin/env python3
#coding = utf-8
print('第二章节')
#n个数的平均值
a = [1,2,3,4,5]
count = 0
s = 0
for i in a:
    s += i
    count += 1
avg = s / count
print('{:.2f}'.format(avg))
#数字宽度 无则空格代替
print("{:5} {:7.2f}".format(avg, avg))
b, c = 2, 1
print('原始值{},{}'.format(b, c))
b, c = c, b
print('交换值{},{}'.format(b, c))
#元组封装与拆分  我理解为对象中各个属性值
d = ('yxd','26','123')
print(d)
name, age, id = d
print('name:{}age:{}id:{}'.format(name, age, id))
#函数divmod(num1,num2)返回元组num1/num2 num1%num2 *拆分元组    str int float
print('{}-{}'.format(*divmod(255, 10)))
#逻辑运算 +-*/% // **


#函数
#斐波拉切数列F(n)
def fibonacciSequence1(n):
    if n <= 2:
        return 1
    else:
        return fibonacciSequence1(n - 1) + fibonacciSequence1(n - 2)

def fibonacciSequence2(n):
    a, b, c = 0, 1, 1
    while c <= n - 1:
        a, b = b, a + b
        c += 1
    return b

print(fibonacciSequence1(7))
print(fibonacciSequence2(7))



# 幂级函数
def powerLevel(x, n):
    a, b, c, d, i = 1, 1, 1, 1, 1
    while i <= n:
         # print('{} {} {} {} {}'.format(a, b, c, d, i))
         b, c, a, d  = b * x, b * x / (d * i), a + b * x / (d * i), d * i
         # print('{} {} {} {} {}'.format(a, b, c, d, i))
         i += 1
    return a

print(powerLevel(0.5, 1))
print(powerLevel(0.5, 3)) 


# 乘法表
def multiplication(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print('{:3} * {:3} = {:3}'.format(i, j, i * j), end = '  ')
            j += 1
        print()
        i += 1

multiplication(10)
# 列表
e = [1, 2, 'a', 'b', 'c', '3']
for i in e:
    print(i)
e[1:2] = []
print(e)
print('{}-{}'.format(e[0:2], e[-3:-1]))
# range产生的是序列 不是列表类型
print(list(range(1, 15, 3))) 
for i in list(range(1, 15, 3)):
    print(i, end = ' ')
else:
    print('done')


# 选棍子
user = ['用户', '电脑']
# 多少种选法
def chooseStick(n, userId):
    if n == 1:
        return 1
    elif n > 4:
        return chooseStick(n - 1, 1 - userId) + chooseStick(n - 4, 1 - userId) + 2
    else:
        return chooseStick(n - 1, 1 - userId) + 1
    
# 用户赢的概率
def userWin(n, userId):
    if n == 1:
        return False
    elif n > 4:
        return not (chooseStick(n - 1, 1 - userId)  and  chooseStick(n - 4, 1 - userId))
    else:
        return not chooseStick(n - 1, 1 - userId)


print(chooseStick(21, 0))
print(userWin(21, 0))
