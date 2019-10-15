#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   56_builtIn_function.py
@Time    :   2019/10/15 18:45
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. abs()  --- 返回数字的绝对值
a11 = 1
a12 = -2
a13 = 0
print("%s 的绝对值为 %s" % (a11, abs(a11)))
print("%s 的绝对值为 %s" % (a12, abs(a12)))
print("%s 的绝对值为 %s" % (a13, abs(a13)))
print("\n")


# 2. divmod() --- 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
a21 = -7
b21 = -2
a22 = 0
b22 = 5
a23 = 20
b23 = 0
print("%s 除以 %s 的；返回结果为：%s" % (a21, b21, divmod(a21, b21)))
print("%s 除以 %s 的；返回结果为：%s" % (a22, b22, divmod(a22, b22)))
# print("%s 除以 %s 的；返回结果为：%s" % (a23, b23, divmod(a23, b23)))
print("\n")


# 3. input & raw_input
# input() 读取一个合法的 python 表达式，输入字符串时必须引号括起来，否则会引发 SyntaxError
# raw_input() 将所有输入作为字符串看待
# 当实际测试下来两个并没有什么区别的感觉
# a31 = input("input: ")
# print("输入的数据为 %s, 它的类型为：%s" % (a31, type(a31)))
# a32 = input("raw_input: ")
# print("输入的数据为 %s, 它的类型为：%s" % (a32, type(a32)))


# 4. open() --- 用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写
#  打开文件的模式：
#       r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#       rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
#       r+	打开一个文件用于读写。文件指针将会放在文件的开头。
#       rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
#       w	打开并只能写入。若文件已存则打开文件并从头开始编辑，原内容会被删除。若该不存在，创建新文件。
#       wb	二进制格式打开文件只用于写入。若文件已存在则打开文件并从头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#       w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#       wb+	以二进制格式打开文件用于读写。如果该文件已存在则打开文件从开头开始编辑原内容会被删除。如果该文件不存在，创建新文件。
#       a	打开文件用于追加。若文件已存在，文件指针放在文件的结尾。新的内容会被写入已有内容。若文件不存在，创建新文件进行写入。
#       ab	二进制格式打开文件用于追加。若文件已存文件指针放在文件结尾。新内容会写入到已有内容。若文件不存在，创建新文件进行写入。
#       a+	打开文件用于读写。若文件已存在文件指针将放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#       ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
# file对象的方法
# file.read([size])         --- 指定大小读取文件，若不写size，则返回整个文件
# file.readline()           --- 返回一行
# file.readlines([size])    --- 返回指定size行，未指定的则返回全部行
# for line in f: print line --- 通过迭代器访问
# f.write["Hello"]          --- 写入字符串数据，若是写入其他类型的数据则需先转换成字符串类型，再写入
# f.tell()                  --- 返回一个整数，表示当前文件指针的位置
# f.seek(偏移量,[起始位置])    --- 用来移动文件指针，偏移量可正可负；起始位置：0-文件头，默认；1-当前位置；2-文件尾
# f.close()                   --- 关闭文件
with open('55_decorators.py', 'r', encoding='utf-8') as f:
    content = f.readline()
    print(content)


# 5. staticmethod()    --- 内置装饰器，返回类的静态函数
class StatiClass(object):
    @staticmethod
    def write():
        print("类的静态方法")


StatiClass.write()
print("\n")


# 6. all() --- 判断给定的可迭代对象参数 iterable 中的所有元素是否都为True，如果全是返回True，不是则为False
# 除了0，空，None，False外都算True
a61 = [1, 2, 3, 4, 5]
a62 = [1, '', '2', 'a']
a63 = [1, 0, '2', 'a']
a64 = [1, False, '2', 'a']
print("%s 的返回：%s" % (a61, all(a61)))
print("%s 的返回：%s" % (a62, all(a62)))
print("%s 的返回：%s" % (a63, all(a63)))
print("%s 的返回：%s" % (a64, all(a64)))
print("\n")
# any() --- 判断给定的可迭代参数iterable是否全为False，则返回 False，如果有一个为True则返回True
b61 = [1, 2, 3, 4, 6]
b62 = [0, 2, 3, 4, 6]
b63 = [0, '', False, None]
print("%s 的返回：%s" % (b61, any(b61)))
print("%s 的返回：%s" % (b62, any(b62)))
print("%s 的返回：%s" % (b63, any(b63)))
print("\n")


# 7. enumerate --- 将可遍历的数据对象（列表、元组或字符串）组合成一个索引序列，同时列出数据和数据下表，多用于for循环
#   enumerate(sequence, [start=0])  --- sequence(一个序列、迭代器或其他支持迭代对象)；start（下标起始位置）
sequence71 = ['A', 'B', 'C']
sequence72 = "I'm a good boy."
sequence73 = (1, 2, 3)
for i, element in enumerate(sequence71):
    print(i, element)
for i, element in enumerate(sequence72):
    print(i, element)
for i, element in enumerate(sequence73):
    print(i, element)
print("\n")


# 8. int()  --- 将一个字符串或数字转换为整型
a81 = 0.1
a82 = 3.8
a83 = -1
a84 = '123'
print("%s 整形为 %s" % (a81, int(a81)))
print("%s 整形为 %s" % (a82, int(a82)))
print("%s 整形为 %s" % (a83, int(a83)))
print("%s 整形为 %s" % (a84, int(a84)))
print("\n")
# str()     --- 返回一个对象的string格式
print(str(123))
print(type(str({"A": 1, "B": 2})))
print("\n")


# 9. ord() --- 是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数
print(ord('a'))
print(ord('b'))
print(ord('C'))
# chr() --- 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
print(chr(123))
print(chr(97))
# unichr() --- 和 chr()函数功能基本一样， 只不过是返回 unicode 的字符
# print(unichr(97))
print("\n")


# 10. eval() --- 用来执行一个字符串表达式，并返回表达式的值
#   eval(expression[, globals[, locals]])
#       expression -- 表达式
#       globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
#       locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
print(eval('3 * 4'))
print(eval('pow(2, 3)'))


# 11. isinstance()  --- 判断一个对象是否是一个已知类型，类似于type()
#       isinstance()会认为子类是一种父类类型，考虑继承关系。
#       type()不会认为子类是一种父类类型，不考虑继承关系
# isinstance(object, classinfo)
a11 = 11
print("%s 的类型为 %s" % (a11, isinstance(a11, int)))
print("%s 的类型为 %s" % (a11, isinstance(a11, (list, int, str))))


class A11(object):
    pass


class A12(A11):
    pass


print(isinstance(A11(), A11))
print(isinstance(A12(), A11))
print(type(A11()) == A11)
print(type(A12()) == A11)
