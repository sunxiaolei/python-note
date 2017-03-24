#!/usr/bin/env python
# -*- coding: utf-8 -*-

'module hello'#任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'xiaolei'#作者

import sys#导入模块

def test():
	args = sys.argv
	print 'Hello%s'%args[:]

#在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败
#最常见的就是运行测试
if __name__ == '__main__':
	test()