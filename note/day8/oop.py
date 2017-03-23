#usr/bin/env python
#-*- coding:utf-8 -*-

#封装
class Person(object):
	#Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
	def __init__(self,name,age):
		self.__name = name
		self.__age = age

	def print_info(self):
		print 'Person:',self.__name,",",self.__age

	def set_name(self,name):
		self.__name = name
	def set_age(self,age):
		self.__age = age
	def get_name(self):
		return self.__name
	def get_age(self):
		return self.__age


p = Person('Jack',25)
p.print_info()
p.set_name('Rose')
p.set_age(18)
print p.get_name(),',',p.get_age()

#继承 多态
class Boy(Person):
	def play(self):
		print 'Playing...'
	def print_info(self):
		print 'Boy:',self.get_name(),',',self.get_age()

b = Boy('Tom',11)
b.print_info()
b.play()

class Girl(Person):
	def play(self):
		print 'Playing...'
	def print_info(self):
		print 'Girl:',self.get_name(),',',self.get_age()

def info(p):
	p.print_info()
info(Person('Jack',25))
info(Girl('Lily',10))
print('\n')
#-----------------------------------------------------------------------------------------------------

#判断对象类型
print type(123)
print type('hehehe')
print type(None)
print type(abs)
print type(b)
print type(type)
#Python把每种type类型都定义好了常量，放在types模块里
import types
print type('123') == types.StringType#True
#判断class类型 
print isinstance(b,Boy)#True
print isinstance(b,Person)#True
print isinstance(p,Girl)#False
print isinstance('hi',str)#True
#还可以判断一个变量是否是某些类型中的一种
print isinstance(12,(str,int))#True

#dir()函数可以获得一个对象的所有属性和方法，返回一个包含字符串的list
print dir(Person)
#getattr()、setattr()、hasattr()
print hasattr(p,'play')#False
print hasattr(Person,'get_age')#True
setattr(p,'eat',"eatting")
print getattr(p,"eat","eat?")#可以传入一个default参数，如果属性不存在，就返回默认值
f = getattr(p,'get_name')#获取方法
print f()