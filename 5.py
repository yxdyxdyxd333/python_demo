#!/usr/bin/env python3
#coding=utf-8

import sys

# 文件操作  open(文件路径，模式rw)
fileObj=open('/usr/local/learn/python/1.txt', 'r')
#print(fileObj)
#print(fileObj.read())
#fileObj.close()
print(fileObj)
print(fileObj.readlines())
fileObj.close()
fileObj=open('/usr/local/learn/python/1.txt', 'r')
print(fileObj)
for i in fileObj:
    print(i)
    print(i, end=' ')
fileObj.close()

fileObj2=open('/usr/local/learn/python/2.txt', 'w')
fileObj2.write('111111\n')
fileObj2.close()
fileObj2=open('/usr/local/learn/python/2.txt', 'r')
print(fileObj2.readlines())

r1 = open('/usr/local/learn/python/1.txt', 'r')
#r11 = r1.readlines()
r2 = open('/usr/local/learn/python/2.txt', 'w')
for i in r1: 
    r2.write(i)
r1.close()
r2.close()

r2 = open('/usr/local/learn/python/2.txt', 'r')
print(r2.read())

with open('/usr/local/learn/python/2.txt', 'r') as r3:
    for i in r3:
        print(i, end = ' ')



with open('/usr/local/learn/python/3.txt', 'w') as r4:
    r4.write('1q2w3e4r5t6y7u8i9o')

a = ''
with open('/usr/local/learn/python/3.txt', 'r') as r5:
    for i in r5.readline():
        if i.isdigit():
            a += i
    print(a)





# try except raise finally
try:
    print('抛出异常')
    raise NameError
except NameError:
    print('抛出异常')
finally:
    print('抛出异常')



print('执行脚本带参数')
print(sys.argv[0])
print(sys.argv[1])


