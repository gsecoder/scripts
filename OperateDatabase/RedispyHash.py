#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RedispyHash.py
@Time    :   2019/12/417:40
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.RedispyConnect import RedisConnect

class RedisHash(object):
	
	def __init__(self):
		self.rc = RedisConnect().redis_connect
		
	def hset_data(self, h, f, v):
		"""
		设置值
		@param h: hash表
		@type h:
		@param f: hash表的域
		@type f:
		@param v: hash表域的值
		@type v:
		@return:
		@rtype:
		"""
		return self.rc.hset(h, f, v)
	
	def hget_data(self, h, f):
		"""
		返回hash表的域值
		@param h:
		@type h:
		@param f:
		@type f:
		@return:
		@rtype:
		"""
		return self.rc.hget(h, f)
	
	def hmset_data(self, k, v):
		"""
		设置多个域的值
		@param k:
		@type v:
		@return:
		@rtype:
		"""
		return self.rc.hmset(k, v)
	
	def hmget_data(self, n, k, *args):
		"""
		获取多个值
		@param k:
		@type k:
		@param args:
		@type args:
		@return:
		@rtype:
		"""
		print(self.rc.hmget(n, k, args))
		
	def get_hkeys(self, n):
		"""
		获取所有的key
		@param n:
		@type n:
		@return:
		@rtype:
		"""
		return self.rc.hkeys(n)
	
	def get_hvals(self, n):
		"""
		获取所有的值
		@param n:
		@type n:
		@return:
		@rtype:
		"""
		return self.rc.hvals(n)
	
	def get_hlen(self, n):
		"""
		获取hash数量
		@param n:
		@type n:
		@return:
		@rtype:
		"""
		return self.rc.hlen(n)
	
	def hdel_data(self, n, f):
		"""
		删除某个域及其值
		@param n:
		@type n:
		@param f:
		@type f:
		@return:
		@rtype:
		"""
		return self.rc.hdel(n, f)
	
	def is_hexist(self, n, f):
		"""
		判断域是否在hash表中
		@param n:
		@type n:
		@param f:
		@type f:
		@return:
		@rtype:
		"""
		return self.rc.hexists(n, f)


if __name__ == "__main__":
	rh = RedisHash()
	# print(rh.rc)

	# 设置值
	# print(rh.hset_data(h="company", f="google", v="www.google.com"))
	# 获取值
	# print(rh.hget_data(h="company", f="google"))
	
	# 设置多值
	# print(rh.hmset_data("company", {"k1": "v1", "k2": "v2"}))
	# 获取多个值
	# rh.hmget_data("company", ["google", "k1"], "k1")
	
	# 获取所有的key
	# print(rh.get_hkeys("company"))

	# 获取所有的值
	# print(rh.get_hvals("company"))
	
	# 获取hash数量
	# print(rh.get_hlen("company"))
	
	# 删除某个域及其值
	# print(rh.hdel_data("company", "google"))
	# print(rh.rc.hkeys("company"))
	
	# 判断域是否在hash表中
	print(rh.is_hexist("company", "k1"))
	print(rh.is_hexist("company", "google"))