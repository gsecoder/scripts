#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : sougou.py
__time__    : 2020/6/24 17:19
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__resume__ : 
"""
# str start end
# abcdefg ab fg
# abcdefg

def str_pro(args_str, start, end):
	list_str = list(str(args_str))
	start_index = list_str.index(start[0]) + 1
	end_index = list_str.index(end[0])
	return_list =  list_str[start_index: end_index]
	return_str = "".join(return_list)
	return return_str

def str_sum(args_str1, args_str2):
	args_str1 = int(args_str1)
	args_st2 = int(args_str2)
	sum_num = args_str1+args_st2
	str_sum_num = str(sum_num)
	return str_sum_num
	
# id name price total
#    mp3  200     4
#    MP3  300     5
#
# sed 's/name/price/p' goods.log

def avage_goods_price(*args_name_type):
	with open("goods.log", 'r', encoding="utf-8") as f:
		items = f.readlines()[1: -1]
		count_num = 0
		count_price = 0
		for item in items:
			item_list = item.split('    ')
			print(item_list)
			if str(args_name_type[0]) in item_list[0] or str(args_name_type[1]) in item_list[0]:
				count_num += 1
				print("count_num: ", count_num)
				count_price += float(item_list[1])
				print("count_price: ", count_price)
		avage_price = count_price / count_num
		return avage_price


if __name__ == '__main__':
	args_type = ['mp3', 'MP3']
	# print(args_type[1])
	print(avage_goods_price(args_type))
    # str_1 = "111"
    # str_2 = "222"
    # print(str_sum(str_1, str_2))
    
    # student(id, name, class, score)
	#
	# SLECT a.id, a.name, b.sum_score,
	# 	IF a.class = "语文" THEN a.score AS '语文',
	# 	IF a.class = "数学" THEN a.score AS '数学',
	# 	IF a.class = "英语" THEN a.score AS '英语'
	# FROM student AS a, (SELECT id, SUM(score) as sum_score FROM student GROUP BY id) AS b
    # WHERE a.id = b.id
 
# if __name__ == '__main__':
#     str_sample = "abcdefg"
#     print(str_pro(str_sample, 'ab', 'fg'))

