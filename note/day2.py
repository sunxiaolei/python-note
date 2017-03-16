#!/usr/bin/env python
# -*- coding: utf-8 -*-

#列表 tuple 创建完毕就不能修改
t = (1,4,'hehe')
print t
#单元素 tuple 要多加一个逗号“,”，避免歧义
t = (2)
print t
t = (2,)
print t
print('\n')
#-----------------------------------------------------------------------------------------------------

#选择 if elif else
#具有相同缩进的代码被视为代码块
score = 80
if score < 60:
	print u'不及格'
elif 60 <= score < 100:
	if score >= 80:
		print u'优秀'
	else:
	 	print u'及格'
else :
	print u'满分'
print('\n')
#-----------------------------------------------------------------------------------------------------

#循环 while
sum = 0;
while True:
	sum = sum + 1
	if sum == 100:
		break
print sum
sum2 = 0;
while sum > 0:
	sum = sum - 1
	if sum % 2 == 0:
		continue
	sum2 = sum + sum2
print sum2
print('\n')
#-----------------------------------------------------------------------------------------------------

#字典dict 用{key:value}表示  
#特点：查找速度快 无论元素多少，速度一样 key不能重复 占用内存大 无序
d = {'a':80,2:50}
print d[2]
#函数len()得出集合大小
print len(d)
#可以先判断是否存在key
if 3 in d:
	print d[3]
else:
	print u'不存在'
#使用get() 不存在则返回None
print d.get(3)
#更新 直接赋值
d['hh'] = 111#没有则直接添加 添加也可以用append()
print d
d['hh'] = 123
print d
print('\n')
#-----------------------------------------------------------------------------------------------------

#set 无序 元素不可重复
#创建 调用 set() 并传入一个 list
s = set([1,4,'t',4])
print s
print 't' in s
#添加
s.add(666)
print s
#删除 删除前最好判断是否存在
if 1 in s:
	s.remove(1)
	print s
else:
	print u'删除失败'
print('\n')
#-----------------------------------------------------------------------------------------------------

#函数
#绝对值
print abs(-5)
#比较 cmp(x,y) x<y:-1 x==y:0 x>y:1
print cmp(2,1)
#转换
print int('333')
print str(89)
#定义函数 def
#没有return语句，函数执行完毕后会返回None。
#return None可以简写为return
def mycmp(x,y):
	if x < y:
		return 1
	elif x == y:
		return 0
	else:
		return -1
print mycmp(2,1)
#函数返回多个值(tuple)
def p(x,y):
	return x + 1,y + 1
print p(5,6)
#汉诺塔
count = 0;
def move(n,a,b,c):
    global count
    if n == 1:
        global count
        print a + '-->' + c
        count += 1
        return
    move(n - 1,a,c,b)
    print a + "-->" + c
    count += 1
    move(n - 1,b,a,c)
move(10, 'A', 'B', 'C')
print count
#遇到错误：UnboundLocalError: local variable 'count' refer enced before assignment
#函数内部对变量赋值修改后，会被Python解释器认为是局部变量而非全局变量 用global声明变量是全局变量
#遇到错误：IndentationError: unindent does not match any outer indentation level
#查看是否该用空格的地方 用了Tab