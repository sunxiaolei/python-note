# !usr/bin/env python
# -*- coding: utf-8 -*-

#读文件
t = open('hi.txt','r')#打开 传入文件名和标示符 标示符'r'表示读
print t.read().decode('utf-8')#读取内容
t.close()#文件使用完毕后必须关闭
#异常捕获
try:
	t = open('h.txt','r')
	print t.read()
except IOError,e:
	print e
finally:
	if t:
		t.close()
#Python引入了with语句来自动帮我们调用close()方法
with open('hi.txt','r') as t:
	print t.read().decode('utf-8')
#调用read()会一次性读取文件的全部内容
#可以反复调用read(size)方法，每次最多读取size个字节的内容
#调用readline()可以每次读取一行内容
#调用readlines()一次读取所有内容并按行返回list
