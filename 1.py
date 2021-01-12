#coding=utf-8
#格式预处理
print('''
换行
换行
''')
#基础数据格式
a='111'
b='222'
print(a+b)
print(a, b)
print('show{}, show{}'.format(a,b))
#name = input('请输入姓名：')
#age = input('请输入年龄')
#print('你叫{}，今年{}岁了'.format(a,b))
c=3.1415926
print('{:.2f}'.format(c))
#条件判断
if a == '111':
    print('a=111')
else:
    print('a!=111')
d = ['星期一','星期二','星期三']
#循环
for i in d:
    print(i)
for i in range(5):
    print(i)
for i in range(8,9):
    print(i)
e = 1
while e <= 10:
    print('出走的{}天'.format(e))
    e += 1
#逢7必过 循环 range 运算法
for i in range(100):
    if i == 7 or i % 10 == 7 or i // 10 == 7:
        print(i)
