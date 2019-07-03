#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_basic_data_types.py
@Time    :   2019/07/03 15:32:37
@Author  :   Crisimple 
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   1.python的基本数据类型：
                （1）数字（int）类型：int、float、complex
                （2）布尔（bloo）类型
                （3）字符串（str）类型
                （4）列表（list）
                （5）元组（tuple）
                （6）字典（dict）
                （7）集合（set）
             2.数据的格式化输出
'''

# here put the import lib

name = input("please input your name: ")
age = int(input("please input your age: "))
sex = bool(int(input("please input your sex: ")))
job = input("please input your job: ")
salary = input("please input your salary: ")

if sex == True:
    sex = 'male'
else:
    sex = 'fmale'

if salary.isdigit():
    salary = int(salary)
else:
    exit("salary must be int.")

print(name, age, sex, job, salary)   

# 格式化输出字符串
personal_info = '''
-------------Personal information of %s---------
.........NAME: %s
.........AGE: %d
.........SEX: %s
.........JOB: %s
.........SALARY: %f
.........WORK STILL: %d YEARS
--------------This is the end-------------
''' % (name, name, age, sex, job, salary, (65-age))

print(personal_info)