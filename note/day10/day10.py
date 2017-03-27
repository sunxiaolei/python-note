# !/usr/bin/env python
# -*- coding:utf-8 -*-

#写
with open('hi.txt','w') as f:
	f.write('Hi\n中文')
#Python内置的os模块可以直接调用操作系统提供的接口函数
import os
print os.name#posix，说明系统是Linux、Unix或Mac OS X，nt，是Windows系统
# 查看当前目录的绝对路径
print os.path.abspath('.')
#创建新文件夹
#os.mkdir('testDir')#已存在会报错
#os.rmdir('testDir')#路径不对 不存在会报错
print('\n')
#-----------------------------------------------------------------------------------------------------

#序列化
#Python提供两个模块来实现序列化：cPickle和pickle。
#这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
#跟cStringIO和StringIO一个道理。用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle
d = dict(name = 'Jack',age = 20)
print pickle.dumps(d)#pickle.dumps()方法把任意对象序列化成一个str
#写入文件
with open('hipickle.txt','w') as f:
	pickle.dump(d,f)
#把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象，
#也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
with open('hipickle.txt','rb') as f:
	print pickle.load(f)
#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
print json.dumps(d)
