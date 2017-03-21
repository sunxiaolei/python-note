#!/usr/bin/env python
# -*- coding: utf-8 -*-

#偏函数
print int('10')#进制转换 默认10进制
print int('10',16)#第二个参数表示需要转换成的进制
def int16(x):
	return int(x,16)#为了方便可以写个函数 直接默认16进制
print int16('10')
#functools.partial可以帮我们创建一个偏函数，不需要自己定义int16()
import functools
int16 = functools.partial(int,base = 16)
print int16('10')
#也可以在函数调用时传入其他值
print int16('10',base = 8)
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
#int16('10')相当于kw = { base: 16 } int('10', **kw)
#max2 = functools.partial(max, 10) 会把10作为*args的一部分自动加到左边
#max2(5, 6, 7)相当于args = (10, 5, 6, 7) max(*args)