#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   11_workpath_pathlib.py
@Time    :   2019/12/2013:53
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   https://www.cnblogs.com/dianel/p/10073718.html
"""

from pathlib import Path
import os
import sys

# 返回当前目录
p = Path()
print("返回当前目录：%s" % p)
print("返回当前目录：%s" % p.cwd())

# 返回当前家目录（当前操作系统的）
print("返回当前家目录：%s" % p.home())

# 判断是否是目录
print("判断是否是目录：%s" % p.is_dir())

# 是否是软链接
print("是否是软链接：%s" % p.is_symlink())

# 是否是块设备
print("是否是块设备：%s" % p.is_block_device())


# 是否是socket文件
print("是否是socket文件：%s" % p.is_socket())

# 是否是绝对路径
print("是否是绝对路径：%s" % p.is_absolute())

# 返回一个新的路径，该路径是当前Path的绝对路径，如果是软连接则被解析
print("返回一个新的路径，该路径是当前Path的绝对路径，如果是软连接则被解析：%s" % p.is_absolute())

# 获取绝对路径，推荐使用resolve()
print("获取绝对路径：%s" % p.absolute())

# 返回一个新的路径，该路径是当前Path的绝对路径，如果是软连接则被解析
print("获取绝对路径：%s" % p.resolve())

# 判断目录或者文件是否存在
print("判断目录或者文件是否存在：%s" % p.exists())

# 删除空目录
# print("删除空目录", p.rmdir())

# 创建一个文件
print("创建一个文件：%s" % p.touch("test.txt"))

# 将路径解析成url
p_u = Path("../usr/local/sbin")
# print("将路径解析成url：%s" % p_u.as_uri())

print("返回操作系统：%s" % os.name)
print("显示当前操作系统的详细信息: (%s, %s, %s, %s, %s)" % os.uname())
print("返回当前的操作系统：%s" % sys.platform)
print("返回目录列表的内容：%s" % os.listdir("./"))
print("修改文件的权限：%s" % os.chmod("10_workpath_os_path.py", 777))

# 返回 p1 下目录的相关信息
p1 = Path("/usr/local/httpd/httpd.conf")
print("目录的最后一个部分，没有后缀p1.name：%s" % p1.name)
print("连接多个字符串到Path对象中-p1.joinpath：%s" % p1.joinpath('test'))
print("目录的逻辑父目录-p1.parent：%s" % p1.parent)
print("父目录序列，索引0是直接的父-p1.parents：%s" % p1.parents[0])
print("父目录序列，索引0是直接的父-p1.parents：%s" % p1.parents[1])
print("父目录序列，索引0是直接的父-p1.parents：%s" % p1.parents[2])
print("父目录序列，索引0是直接的父-p1.parents：%s" % p1.parents[3])
print("目录中的最后一部分-p1.stem：%s" % p1.stem)
print("目录中的最后一部分的扩展名-p1.suffix：%s" % p1.suffix)
print("返回多个扩展名列表-p1.suffixes：%s" % p1.suffixes)
print("返回路径中的每一个部分-p1.parts：(%s, %s, %s, %s, %s)" % p1.parts)
print("补充扩展名到路径的尾部，返回新的路径，扩展名存在则无效-p1.with_suffix(suffix)：%s" % p1.with_suffix('.txt'))
print("替换目录最后一个部分并返回一个新的路径-p1.with_name(name)：%s" % p1.with_name("httpd.txt"))


