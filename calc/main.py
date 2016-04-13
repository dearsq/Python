#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re

# 处理乘除的方法
def compute_mul_div(arg):
	pass
	
# 处理加减的方法
def compute_add_sub(arg):
	pass

# 计算最简表达式的方法
def compute(expr):
	pass


# 括号处理方法
def bracket(expr):
	# 先匹配最层的括号
	# 如果没有括号，直接返回表达式
	if not re.search('\(([\+\-\*\/]*\d+\.*\d*)+\)',expr):
		return expr
		
	# 如果有括号，取出最里面一个括号的内容，得到新的表达式
	new_expr = re.search('\(([\+\-\*\/]*\d+\.*\d*)+\)',expr).group()
	
	#去掉两侧的括号，获得中间的表达式
	new_expr_no_bracket= new_expr[1:len(new_expr)-1]
	
	# 将 expr 按内容进行分割，得到（before，匹配内容，after）得到 content 两侧的内容，并且赋值给 before，after
	new_list = re.split('\(([\+\-\*\/]*\d+\.*\d*)+\)',expr)
	before = new_list[0]
	after = new_list[2]
	
	# 将 new_expr_no_bracket 进行计算，求得 result
	result = compute(new_expr_no_bracket)
	
	# 将  before + middle + after 拼接，得到新的表达式
	re_expr = "%s%s%s" %(before,result,after)
	
	return bracket(re_expr)
	
	
def is_format_right(expr):
	if expr.count('(') == expr.count(')'):
		return True
	else:
		print("FORMAT ERROR")
		return False
	
# main
if __name__ == "__main__":	
	# sys.argv[0]为文件名 main.py  sys.argv[1]为计算式表达式
	#测试时先屏蔽 str = sys.argv[1]
	str = "1+  2 -3+ 4"
	
	str_no_space = re.sub('\s*','',str)
	
	# 输入表达式的格式正确性判断
	is_format_right(str_no_space)
	
	
	
	# 先处理所有的括号，取出括号内的部分
	ret = bracket(str_no_space)