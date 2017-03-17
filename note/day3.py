#!/usr/bin/env python
# -*- coding: utf-8 -*-

#默认参数 默认参数只能定义在必需参数的后面
def m(x,y = 10):
	return x+y
print m(1)
print m(1,1)
#可变参数 Python解释器把传入的一组参数组装成一个tuple传递给可变参数
def c(*x):
	print x
c(2,4,4,'lol')
print('\n')
#-----------------------------------------------------------------------------------------------------

#切片 list[a:b]从索引a开始取，直到索引b  第一个索引为0 越界不会报错 
list = ['1','2','3','4','5']
print list[0:2]
#[:]]，表示从头到尾 [:b] 从0到b [a:] 从a到最后
print list[:]
#list[a:b:n] 每n个取一个
print list[1:4:2]
#支持倒数切片 倒数第一个索引为-1
print list[-3:-1]
#字符串切片
str = 'abcdefg'
print str[1:4]
#字符串upper()方法 小写转大写
print str.upper()
print str[0].upper()+str[1:]#第一个字母大写
print('\n')
#-----------------------------------------------------------------------------------------------------

#索引迭代 enumerate()
#迭代的每一个元素实际上是一个tuple
list = ['a','b','c']
for x in enumerate(list):
	print x
for p,x in enumerate(list):
	print p,'-->',x
#zip()函数可以把两个 list 变成一个 list 
list2 = [1,2,4]
print zip(list,list2)
#迭代dict key
d = {'a':2,'b':5,'c':9}
for x in d:
	print x
#迭代dict value
#values() 方法实际上把一个 dict 转换成了包含 value 的list
#itervalues() 方法不会转换，它在迭代过程中依次从 dict 中取出 value，节省了生成 list 所需的内存
for x in d.values():
	print x
for x in d.itervalues():
	print x
#迭代dict的key和value
for x,y in d.items():
	print x,':',y
for x,y in d.iteritems():
	print x,':',y
print('\n')
#-----------------------------------------------------------------------------------------------------

#生成列表
#生成[1*1,2*2,...n*n]
def c(n):
	return [x*x for x in range(1,n+1)]
print c(10)
#[1x2, 3x4, 5x6, 7x8, ..., n*(n+1)]
def c(n):
	return [x*(x+1) for x in range(1,n+1,2)]
print c(100)
#条件过滤
def c(n):
	return [x*(x+1) for x in range(1,n+1) if x%2!=0]
print c(100)
#多层
list = [x+y for x in ['a','b','c'] for y in ['A','B','C']]
print list
#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
l = [100*x+10*y+z for x in range(1,10) for y in range(0,10) for z in range(1,10) if x == z]
print l
#列出当前列表文件和目录
import os
print [d for d in os.listdir('.')]
print('\n')
#-----------------------------------------------------------------------------------------------------

#高阶函数
#变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
mm = abs
print mm(-1)
def absadd(x,y,f):
	return f(x)+f(y)
print absadd(-5,-3,mm)