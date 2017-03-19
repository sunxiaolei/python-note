#!/usr/bin/env python
# -*- coding: utf-8 -*-

#map()函数 
#接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def format_name(s):
    return s[0].upper()+s[1:].lower()
print map(format_name, ['adam', 'LISA', 'barT'])#['Adam','Lisa','Bart']
print('\n')
#-----------------------------------------------------------------------------------------------------

#reduce()函数
#reduce()函数必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
#还可以接收第3个可选参数，作为计算的初始值
def sum(x,y):
	return x+y
l = [1,2,3,4,5]
print reduce(sum,l)#15
print reduce(sum,l,100)#115
print('\n')
#-----------------------------------------------------------------------------------------------------

#filter()函数
#接收一个函数 f 和一个list，f 对每个元素进行判断，返回True或False，filter()返回符合条件元素组成的新list
def f(x):
	return x%2 == 0
l = [1,2,3,4,5,6,7,8,9]
print filter(f,l)#[2,,6,8]
print('\n')
#-----------------------------------------------------------------------------------------------------

#sorted()函数
#接收一个比较函数来实现自定义排序
#比较函数是，传入两个待比较的元素 x , y , x 在 y 的前面，返回-1，后面，返回 1。相等，返回 0
#忽略大小写排序
l = ['bob', 'Zoo', 'about', 'Credit']
def c(x,y):
	return cmp(x.lower(),y.lower())
print sorted(l,cmp)
print('\n')
#-----------------------------------------------------------------------------------------------------

#返回函数
def c_sum(l):
	def lazy_sum():
		return sun(l)
	return lazy_sum
print c_sum([1,2,3,4])
