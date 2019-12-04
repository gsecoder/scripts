#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   RedispySet.py
@Time    :   2019/12/415:25
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from OperateDatabase.RedispyConnect import RedisConnect


class RedisSets(object):

    def __init__(self):
        self.rc = RedisConnect().redis_connect
        
    def sadd_data(self, k, *args):
        """
        添加元素
        @param k:
        @type k:
        @param v:
        @type v:
        @return:
        @rtype:
        """
        return self.rc.sadd(k, args)
    
    def smembers_get(self, k):
        """
        返回集合中的所有元素
        @param k:
        @type k:
        @return:
        @rtype:
        """
        return self.rc.smembers(k)
    
    def srem_data(self, k, v):
        """
        删除元素
        @param k:
        @type k:
        @param v:
        @type v:
        @return:
        @rtype:
        """
        return self.rc.srem(k, v)
    
    def sismember_get(self, k, v):
        """
        判读是否为集合的元素
        @param k:
        @type k:
        @param v:
        @type v:
        @return:
        @rtype:
        """
        return self.rc.sismember(k, v)
    
    def sdiff_get(self, k1, k2):
        """
        返回两个集合的差集，以位置1的集合为基准看
        @param k1:
        @type k1:
        @param k2:
        @type k2:
        @return:
        @rtype:
        """
        return self.rc.sdiff(k1, k2)
    
    def sinter_get(self, *args):
        """
        SINTER返回几个集合的交集
        @param args:
        @type args:
        @return:
        @rtype:
        """
        return self.rc.sinter(args)
    
    def sunion_get(self, *args):
        """
        SUNION返回几个集合的并集
        @param args:
        @type args:
        @return:
        @rtype:
        """
        return self.rc.sunion(args)


if __name__ == "__main__":
    rs = RedisSets()
    # print(rs.rc)

    # 添加一个元素
    # print(rs.sadd_data("set1", "v2"))
    # 添加重复元素
    # print(rs.sadd_data("set1", "v2"))
    # 添加多个元素
    # print(rs.sadd_data("set2", "v3", "V4", "V5"))
    
    # 返回集合中的所有元素
    # print(rs.smembers_get("set1"))

    # 删除元素
    # rs.srem_data("set1", 'v1')
    # print(rs.smembers_get("set1"))
    
    # 判断是否是集合元素
    # print(rs.rc.smembers("set1"))
    # print("是集合元素：%s" % rs.sismember_get("set1", ('v2',)))
    # print("不是集合元素：%s" % rs.sismember_get("set1", ('v22', )))
    
    # 差集
    # print(rs.rc.smembers("set1"))
    # print(rs.rc.smembers("set2"))
    # print(rs.sdiff_get("set1", "set2"))
    # print(rs.sdiff_get("set2", "set1"))
    
    # 交集
    # print(rs.rc.smembers("set1"))
    # print(rs.rc.smembers("set2"))
    # print(rs.sinter_get("set1", "set2"))
    
    # 并集
    print(rs.rc.smembers("set1"))
    print(rs.rc.smembers("set2"))
    print(rs.sunion_get("set1", "set2"))
