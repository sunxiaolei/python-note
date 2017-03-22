# usr/bin/env python
# -*- coding:utf-8 -*-

'test PIL'
#pip install PIL 安装PIL (Python Imaging Library ) 提示
#Could not find a version that satisfies the requirement PIL (from versions: )  
#No matching distribution found for PIL  
#pip search PIL
#出现  Pillow (3.2.0)         Python Imaging Library (Fork) 名字变了
#安装：pip install Pillow
from PIL import Image#Pillow由PIL而来，所以该导入该库使用import PIL）
img = Image.open('python-logo.png')
print img.format,img.size,img.mode
img.thumbnail((50,50))
img.save('logo50.jpg','JPEG')