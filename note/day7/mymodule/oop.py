#usr/bin/env python
# -*- coding:utf-8 -*-

'Person Object'

class Person(object):
	def __init__(self,name,age):#注意__init__方法的第一个参数永远是self，表示创建的实例本身
		self.name = name
		self.age = age
	def printinfo(self):
		print self.name,self.age

#有了__init__方法，在创建实例的时候，必须传入与__init__方法匹配的参数
#但self不需要传，Python解释器自己会把实例变量传进去
p = Person('Jack',20)
print p.name,p.age
p.printinfo()