#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   03_workpath_shutil.py
@Time    :   2019/12/21上午11:43
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import shutil

src = ""
dst = ""
olddir = ""
newdir = ""
# 从源src复制到dst中去。 如果当前的dst已存在的话就会被覆盖掉
shutil.copyfile(src, dst)
# 移动文件或重命名
shutil.move(src, dst)
# 只是会复制其权限其他的东西是不会被复制的
shutil.copymode(src, dst)
# 复制权限、最后访问时间、最后修改时间
shutil.copystat(src, dst)
# 复制一个文件到一个文件或一个目录
shutil.copy(src, dst)
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2(src, dst)
# 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copy2(src, dst)
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.copytree(olddir, newdir, True)
# 递归删除一个目录以及目录内的所有内容
shutil.rmtree(src )



