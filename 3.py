#!/usr/bin/env python3
#coding=utf-8
# 列表相关操作
a = [9, 8, 7, 6, 5, 4, 4, 3, 2, 1]
# 某个元素个数
print(a.count(4))
# 追加元素
a.append(0)
a.insert(0, -1)
print(a)
# 排序
a.sort()
print(a)
b = ['a', 'b', 'c']
# 追加
a.extend(b)
# 删除
a.remove(5)
del a[5]
print(a)


# 列表作为栈
a.pop()
print('后进先出{}'.format(a))
a.pop(0)
print('pop出特定位置元素，可作为队列，先进先出每次出0位置上的{}'.format(a))
a.append('d')
print(a)

# 列表推导式 c 等价于 d
c = [x + y for x in range(5) for y in range(5) if x != y]
print(c)
d = []
for x in range(5):
    for y in range(5):
        if x != y:
            d.append(x + y)
print(d)
e = [x ** 2 for x in [y for y in range(1,5)]]
print(e)
print(type(e))


# 元组相关操作 赋值 元组封装 元组拆分 不可变类型无法删除编辑
f = ('a','b','c')
g = divmod(15, 2)
h, i = divmod(15, 2)
j = 321,
print('{}-{}-{}-{}-{}-{}'.format(f, g, h, i, j, type(j)))

# 集合相关操作 不包含重复元素 存在k不存在l 同时存在 存在k或者l中  存在k或l中的一个
a = {'a', 'b', 'c', 'a'}
k = set('abcdfrfff12ert45')
l = set('abcdfrfff')
l.add('mmmmgggg')
l.pop()
print('{} - {} - {} - {}'.format(a, k, l, k - l, k & l, k | l, k ^ l))
print('a' in a)

# 字典相关操作(键值对) 赋值 删除键值对 遍历
m = {'name':'holly', 'age':'26'}
print(m)
m['holly'] = '123'
print(m)
del m['holly'] 
print(m)
print('holly' in m)

n = dict((('name','ace'),('age','25')))
n.setdefault('id', []).append('1')
for x, y in n.items():
    print('{} -- {}'.format(x, y))
    
print(n.get('id', '234'))


# 序列遍历  1带索引遍历 2两个同时遍历
for i, j in enumerate(range(5)):
    print('{} - {}'.format(i, j))


for i, j in zip(a, b):
    print('{} - {}'.format(i, j))
