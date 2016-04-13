#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re

# 处理乘除的方法
def compute_mul_div(arg):
	# 接受一个 arg 列表
	# 其第一个元素为待处理表达式
	# 其第二个元素为我们进行提取的次数
	value = arg[0]
	# 对字符串进行乘除匹配，忽略掉加减
	mch = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value)
	# 没有匹配就直接返回
	if not mch:
		return
	# 有匹配则将其内容保存在 content 中
	content = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value).group()
	# 进行 * / 判断并计算
	if len(content.split('*'))>1:
		n1,n2 = content.split('*')
		get_value = float(n1)*float(n2)
	else:
		n1,n2 = content.split('/')
		get_value = float(n1)/float(n2)
	# 取出刚才所计算的内容之外 两头的内容 before,after
	before,after = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*',value,1)
	# 和算好的结果拼接成新的字符串
	re_str = "%s%s%s" %(before,get_value,after)
	# 把 new_str 赋值到 arg[0] 中
	arg[0] = re_str
	# 递归算出最终结果
	compute_mul_div(arg)

	
# 处理加减的方法
def compute_add_sub(arg):
	# 接受一个 arg 列表
	# 其第一个元素为待处理的表达式
	# 表达式中 可能存在 ++\--\+-\-+ 的情况，需要处理
	
	while True:
		if arg[0].__contains__('--') or arg[0].__contains__('+-') or arg[0].__contains__('--') or arg[0].__contains__('-+'):
			arg[0] = arg[0].replace('--','+')
			arg[0] = arg[0].replace('++','+')
			arg[0] = arg[0].replace('-+','-')
			arg[0] = arg[0].replace('+-','-')
		else:
			break
	
	# 然后对 arg[0] 表达式进行第二次处理
	# 提取首位为 "-",并将提取的次数保存在 arg[1] 中
	# 每提取一次，表达式中所有的 "+" 替换成 "-" "-"替换成"+"
	# 然后取 arg[0] 表达式字符串中的每一位即可赋值给 arg[0]
	if arg[0].startswith('-'):
		arg[1]+= 1
		arg[0] = arg[0].replace('-','&')
		arg[0] = arg[0].replace('+','-')
		arg[0] = arg[0].replace('&','+')
		arg[0] = arg[0][1:]
	value = arg[0]
	#对字符串的 value 进行匹配，匹配 + 或者 - 两边的内容，如 1+2-3，就匹配 1 + 2
	mch = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value)
	# 如果没匹配到就直接返回
	if not mch:
		return
	# 匹配到就将内容保存在 content 中
	content = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*',value).group()
	# 进行计算
	if len(content.split('+'))>1:
		n1,n2 =content.split('+')
		get_value = float(n1)+float(n2)
	else:
		n1,n2 =content.split('-')
		get_value = float(n1)-float(n2)
	# 取出两头的内容，和计算后的结果重新拼接
	before,after = re.split('\d+\.*\d*[\+\-]{1}\d+\.*\d*',str(value),1)
	re_str = "%s%s%s" %(before,get_value,after)
	arg[0] = re_str
	compute_add_sub(arg)
		
	
# 计算最简表达式的方法
def compute(expr):
	print("Younix,Now Compute start")
	inp = [expr,0]
	print("Younix",inp)
	# 先乘除
	compute_mul_div(inp)
	# 后加减
	compute_add_sub(inp)
	# 判断 inp[1] 是奇数还是偶数，确定正负
	print("Younix",inp)

	count = divmod(inp[1],2)
	print("Younix",inp[0])
	result = float(inp[0])
	if count[1] == 1:
		result = result * (-1)
	
	print("Younix,Now Compute end")
	return result


# 括号处理方法
def bracket(expr):
	print("Younix,Now bracket start")
	# 先匹配最层的括号
	# 如果没有括号，直接返回表达式
	if not re.search('\(([\+\-\*\/]*\d+\.*\d*)+\)',expr):
		print("Younix,Now bracket end")
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
	if expr.count('(') != expr.count(')'):
		print("FORMAT ERROR")
		return False
	elif expr.endswith("-") or expr.endswith("+") or expr.endswith("*") or expr.endswith("/") or expr.endswith("^"):
		print("FORMAT ERROR")		
		return False
	else:
		print("Younix,format is true")
		return True
	
# main
if __name__ == "__main__":	
	# sys.argv[0]为文件名 main.py  sys.argv[1]为计算式表达式
	#测试时先屏蔽 my_str = sys.argv[1]
	my_str = "1+(2-3)+4+(1+2)"
	
	str_no_space = re.sub('\s*','',my_str)
	# print(str_no_space)
	
	# 输入表达式的格式正确性判断
	is_format_right(str_no_space)
	
	# 先处理所有的括号，取出括号内的部分
	ret = bracket(str_no_space)
	
	final = compute(ret)
	
	print(final)
	
	