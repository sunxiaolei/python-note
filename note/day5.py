#!/usr/bin/env python
# -*- coding: utf-8 -*-

#返回函数  Python中，一切皆对象！！！
def l_sum(l):
	def lazy_sum():
		return sum(l)
	return lazy_sum
l = [1,2,3,4]
f = l_sum(l)#返回的是函数
print f()#调用函数
#闭包
def count():
	fs = []
	for x in range(1,4):
		def f():
			return x
		fs.append(f)
	return fs
f1,f2,f3 = count()
print f1(),f2(),f3()#3 3 3
#返回的函数引用了变量x，但并非立刻执行。等到3个函数都返回时，x已经变成了3，因此最终结果为3
#注意：返回函数不要引用任何循环变量，或者后续会发生变化的变量！！！
#一定要引用就再创建一个函数，参数绑定循环变量当前的值
def count():
	fs = []
	for x in range(1,4):
		def f(i):
			def g():
				return i
			return g
		fs.append(f(x))
	return fs
f1,f2,f3 = count()
print f1(),f2(),f3()#1 2 3
print('\n')
#-----------------------------------------------------------------------------------------------------

#匿名函数
print map(lambda x:x+1,[1,2,3,4])
#lambda x:x+1 表示 def f(x): return x+1
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x:x+1
print map(f,[1,2,3,4])
#也可以是返回值
def f():
	return lambda x:x+1
print map(f(),[1,2,3,4])
print('\n')
#-----------------------------------------------------------------------------------------------------

#装饰器
#函数对象有一个__name__属性，可以拿到函数的名字
def fun():
	return 'a'
f = fun
print f.__name__#fun
#假设要增强fun()函数的功能，例：在函数调用前后自动打印日志，但又不修改now()函数的定义
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(f):
	def wrapper(*args, **kw):#参数定义是(*args, **kw)，可以接受任意参数的调用
		print "log--function-->%s()"%f.__name__
		return f(*args, **kw)
	return wrapper
@log#相当于执行了test = log(test)
def test(x):
	print 'test%s'%x
test("666")
#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log(text):
	def decotator(func):
		def wrapper(*args,**kw):
			print 'Log--%s-->%s'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decotator
@log('test2')
def test(x):
	print 'test%s'%x
test('777')
#问题：经过decorator装饰之后的函数，它们的__name__已经从原来的变成了'wrapper'
print test.__name__#wrapper
#Python内置的functools.wraps可以解决这个问题
import functools
def log(text):
	def decotator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'Log--%s-->%s'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decotator
@log('test2')
def test(x):
	print 'test%s'%x
print test.__name__#test