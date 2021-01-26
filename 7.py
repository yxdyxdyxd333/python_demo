#!/usr/bin/env python3
#coding=utf-8

from collections import Counter, defaultdict, namedtuple
import re

Person = namedtuple('Person', ['name', 'age'])
p = Person('Holly', 26)
print(p)
name, age = p  #元组拆分
print('{} ----- {}'.format(name, age))


path='/usr/local/learn/python/1.txt'
words = re.findall('\w+', open(path).read().lower())
print(words)
print(Counter(words).most_common())

words = Counter(i=5, b=3, c=4, d=0)
print(words)
print(list(words.elements()))


s = [('a', 3), ('b', 4), ('c', 5)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())
