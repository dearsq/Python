#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re

# main
if __name__ == "__main__":	
	# sys.argv[0]为文件名 main.py  sys.argv[1]为计算式表达式
	#测试时先屏蔽 str = sys.argv[1]
	str = "1+  2 -3+  4"
	
	str_no_space = re.sub('\s*','',str)
	
	print(str_no_space)