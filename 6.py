#!/usr/bin/env python3
#coding=utf-8

import utils
from common import fun1
from modualtest import common1
import os
import requests

#类相关
class Person(object):
    def __init__(self, name):
        self.name = name
#继承
class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age
    @property
    def getInfo(self):
        return (self.name, self.age)
    
    @property
    def age1(self):
        return self.age
     
    @age1.setter
    def age1(self, value):
        print(value)
        if(value > 0):
            self.age = value
        else:
            print('age is not larger then 0')
            return
            


if  __name__ ==  '__main__':
    #创建对象
    x = Person('holly')
    print(x.name)
    y = Child('HHH', 5)
    print(y.name, y.age)
    #删除对象
    del x
    print(y.getInfo)
    y.age = 10
    print(y.age1)
    y.age = -10
    print(y.age1)
    print(utils.avg(3, 4)) # 导入整个模块
    print(fun1()) #导入模块某些方法
    #print(fun2)
    #print(modualtest.common1())
    
    names = os.listdir('./')
    names.sort()
    for name in names:
        print(name, end= ' ')
    print('=====')
    print(os.getpid())
    result = requests.get('http://baidu.com')
    print(result)
