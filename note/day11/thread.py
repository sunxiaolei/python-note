# !/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
print os.getpid()
#Unix/Linux操作系统提供了一个fork()系统调用
#fork()调用一次，返回两次,操作系统自动把当前进程（称为父进程）复制了一份（称为子进程）
#分别在父进程和子进程内返回
#子进程永远返回0，而父进程返回子进程的ID。
#一个父进程可以fork出很多子进程，而子进程只需要调用getppid()就可以拿到父进程的ID
#Windows没有fork调用，代码在Windows上无法运行。
#由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的 

#multiprocessing模块就是跨平台版本的多进程模块。
#multiprocessing模块提供了一个Process类来代表一个进程对象

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
#创建子进程时，需要传入一个执行函数和函数的参数
#创建一个Process实例，用start()方法启动
#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步