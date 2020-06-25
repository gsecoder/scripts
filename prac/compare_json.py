#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : compare_json.py
__time__    : 2020/6/24 15:06
__author__  : crisimple
__github__ :  https://crisimple.github.io/
__resume__ : 
"""

def compare_json(src_data, dst_data):
	if isinstance(src_data, dict):
		for key in src_data:
			if key not in dst_data:
				print("dst_data 不存在 src_data 中的key: ", key)
				
		for key in src_data:
			if key in dst_data:
				if src_data[key] == dst_data[key]:
					compare_json(src_data[key], dst_data[key])
				else:
					print("src_data[%s]=%s != dst_data[%s]=%s" % (key, src_data[key], key, dst_data[key]))
			else:
				print("dst_data 不存在 key: %s" % key)
				
	elif isinstance(src_data, list):
		if len(src_data) == len(dst_data):
			for key in range(len(src_data)):
				if src_data[key] == dst_data[key]:
					compare_json(src_data[key], dst_data[key])
				else:
					print("不相等")
		else:
			print("不相等")
			
	else:
		if str(src_data) == str(dst_data):
			print("相等")
		else:
			print("不相等")
			

if __name__ == '__main__':
	src_data_sample = "1"
	dst_data_sample = ""
	compare_json(src_data_sample, dst_data_sample)
	