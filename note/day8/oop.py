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
print('\n')
#-----------------------------------------------------------------------------------------------------

#创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
b.height = 120#动态绑定一个属性
print b.height
def set_height(self,height):
	self.height = height
from types import MethodType
b.set_height = MethodType(set_height,b,Boy)	#动态绑定一个方法
b.set_height(100)
print b.height
#给一个实例绑定的方法，对另一个实例是不起作用的
#可以给class绑定方法
Boy.set_height = MethodType(set_height,None,Boy)
b2 = Boy('Harry',11)
b2.set_height(90)
print b2.height

#限制class的属性
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性 继承无效
class Girl(Person):
	__slots__ = ("height",)
#测试发现 父类不包含__slots__定义 只有子类定义 不起作用？
g = Girl('Lily',11)
g.weight = 50
print g.weight#正常打印
class Person(object):
	__slots__ = ()
class Girl(Person):
	__slots__ = ("height",)
g = Girl()
#g.weight = 50
#print g.weight#AttributeError: 'Girl' object has no attribute 'weight'

class Person(object):
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,value):
		self._name = value

p = Person()
p.name = 'Jack'
print p.name
#只定义@property，就是一个只读属性
print('\n')
#-----------------------------------------------------------------------------------------------------

#多继承
class Person(object):
	pass
class Student(Person):
	@property
	def student(self):
		print "go to school"
	def eat(self):
		print "Student eat"
class Man(Person):
	@property
	def man(self):
		print "man"
	def eat(self):
		print "Man eat"
class Boy(Man,Student):
	pass
b = Boy()
b.student
b.man
b.eat()#测试 都有的方法 实现的是第一个继承的父类的方法
print('\n')
#-----------------------------------------------------------------------------------------------------

#定制类 一些方法
#__str__ 相当于Java中的toString()
class Person(object):
	def __str__(self):
		return "This is a Person"
p = Person()
print p