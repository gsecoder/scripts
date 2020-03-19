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
# --------------------------------
# bin()     --- 返回一个整数int或长整型long int的二进制表示
bin_1 = 10
bin_2 = 20
print("%s经过bin后返回%s" % (bin_1, bin(10)))
print("%s经过bin后返回%s" % (bin_2, bin(20)))
print("\n")
# --------------------------------
# max() --- 返回给定参数的最大值，参数可以为序列
print("返回序列的最大值：", max(100, 200, 3000, 800))
print("\n")
# --------------------------------
# min() --- 返回给定参数的最小值，参数可以为序列
print("返回序列的最小值：", min(-100, 200, 0, -10000))
print("\n")
# ---------------------------------
# reversed()    --- 用于反向列表元素
reverse_list = [3, 5, 7, 1]
reversed_tuple = (1, 4, 3, 5)
reverse_list.reverse()
print("%s 的反向输出为：%s" % (reverse_list, reverse_list))
# print("%s 的反向输出为：%s" % (reversed_tuple, reversed_tuple))
print("\n")
# -----------------------------
# oct() --- 将一个整数转换成8进制字符串
print("返回八进制的字符串：", oct(10))
# -----------------------------
# zip() --- 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
zip_1 = [1, 2, 3]
zip_2 = [4, 5, 6]
zip_3 = [7, 8, 9]
zipped1 = zip(zip_1, zip_2)
zipped2 = zip(zip_3, zip_2)
print("压缩成数组：", zipped1)
print("解压数组：", zip(*zipped2))
print("\n")
# -----------------------------
# complex([real[, imag]])   创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
#   real -- int, long, float或字符串
#   imag -- int, long, float
print("返回一个复数：", complex(1, 2))
print("返回一个复数：", complex("1+2j"))
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
#  pow(x, y) --- 返回x的y次方的值
c31 = 2
cc31 = -3
c32 = 2
cc32 = 3
print("%s 的 %s 次幂运算为：%s" % (c31, cc31, pow(c31, cc31)))
print("%s 的 %s 次幂运算为：%s" % (c32, cc32, pow(c32, cc32)))
print("\n")
# ---------------------------------------------------------
# sum(iterable[, start]) --- 对一系列数据求和
#   iterable --- 可迭代对象：列表、元组、集合
#   start --- 指定增加的参数，如果没有设置这个值，默认为0
sum_1 = [0, 1, 2, 3]
sum_2 = (9, 1, 2, 3)
sum_3 = {9, 1, 2, 0}
print("%s 求和结果为：%s" %(sum_1, sum(sum_1)))
print("%s 求和结果为：%s" %(sum_2, sum(sum_2)))
print("%s 求和结果为：%s" %(sum_3, sum(sum_3)))
print("\n")
# --------------------------------------------
# sorted(iterable, cmp=None, key=None, reverse=False)
#   iterable -- 可迭代对象
#   cmp -- 比较的函数有两个参数，参数的值从可迭代对象中取出，函数必须遵守，大于返回1，小于则返回-1，等于则返回0
#   key -- 用来进行比较的元素，只有一个参数，函数的参数取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
#   reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）
sorted_dict = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print("排序结果为：", sorted(sorted_dict, key=lambda s: s[2], reverse=True))
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
# file()    --- 用于创建file对象，它有一个别名叫open()
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
print("\n")


# 5. staticmethod    --- 内置装饰器，返回类的静态函数
class StatiClass(object):
    @staticmethod
    def write():
        print("类的静态方法")
StatiClass.write()
print("\n")
# -------------------------------------
# classmethod   --- 内置装饰器修饰的函数不需要实例化，第一个参数由self变为cls，用来调用类的属性、类的方法、
class ClassMethod(object):
    bar = 1
    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print(cls.bar)
        cls().func1()

ClassMethod.func2()
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
# iter(object[, sentinel])    --- 生成迭代器
iter_1 = [1, 2, 3, 4, 5, 6]
iter_2 = "xiao"
for i in iter_1:
    print("=====%s" % i)
print("**************", next(iter(iter_2)))
print("**************", next(iter(iter_2)))
print("**************", next(iter(iter_2)))
print("**************", next(iter(iter_2)))
print("\n")
# -----------------------------
# next() --- 返回迭代器的下一个项目
next_1 = iter([1, 2, 3, 4])
while True:
    try:
        x = next(next_1)
        print("next访问迭代器的数据：", x)
    except StopIteration:
        break
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
# --------------------------------------------------------------
# tuple()   --- 将列表转换为元组
tuple_1 = [1, 2, 3, 7]
print("tuple()将 %s 转换成元组后为：%s" % (tuple_1, tuple(tuple_1)))
print("\n")
# --------------------------------
# list()    --- 将元组转换为列表
list_1 = (1, '2', 'xyz', 7)
print("list()将 %s 转换成列表后为：%s" % (list_1, list(list_1)))
print("\n")
# --------------------------------
# slice(start, stop, step) --- 实现切片对象，用在切片操作函数里的参数传递
slice_list = [1, 2, 3, 4, 5, 6, 7]
myslice = slice(1, 6, 2)
print("slice截取列表：", slice_list[myslice] )
print('\n')
# --------------------------------
# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)
print("字典1：", dict())
print("字典1：", dict(a='1', b=2, c=3))
print("字典1：", dict(zip(['AA', 'BB', 'CC'], [11, 22, 33])))
print("字典1：", dict([("AAA", 111), ('BBB', 222), ('CCC', 333)]))
print("\n")
# --------------------------------
# bool()    --- 将给定参数转换为布尔类型，如果没有参数，返回False
bool_1 = 0
bool_2 = 1
bool_3 = None
bool_4 = ''
bool_5 = 'A'
print("bool() 将 %s 转换为bool类型后为：%s" % (bool_1, bool(bool_1)))
print("bool() 将 %s 转换为bool类型后为：%s" % (bool_2, bool(bool_2)))
print("bool() 将 %s 转换为bool类型后为：%s" % (bool_3, bool(bool_3)))
print("bool() 将 %s 转换为bool类型后为：%s" % (bool_4, bool(bool_4)))
print("bool() 将 %s 转换为bool类型后为：%s" % (bool_5, bool(bool_5)))
print("\n")
# --------------------------------
# float()   --- 将整数和字符串转换成浮点数
print("整数转换为浮点数：", float(12))
print("字符串转换为浮点数：", float('234'))
print("\n")
# --------------------------------
# set(iterable)   --- 创建一个无序不重复的元素集，iterable可迭代对象
#       --- 可进行关系测试，删除重复数据，还可以计算并集、交集、差集等
set_1 = set("HELLO")
set_2 = set("WORLD")
print("原集合分别为：%s %s" % (set_1, set_2))
print("%s & %s 的结果为：%s" % (set_1, set_2, set_1 & set_2))
print("%s | %s 的结果为：%s" % (set_1, set_2, set_1 | set_2))
print("%s - %s 的结果为(即前面有后面没有的)：%s" % (set_1, set_2, set_1 - set_2))
print("\n")
# --------------------------------
# map(function,iterable,...)    --- 会根据提供的函数对指定序列做映射
map_result = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print("map函数返回", map_result)
print("\n")
# --------------------------------
# repr()    --- 将对象转换为供解释器读取的形式
repr_dict = {"A": 1, "B": 2}
print("repr返回对象的string形式：", repr(repr_dict))
print("\n")
# --------------------------------
# hash() ---    获取取一个对象（字符串或者数值等）的哈希值
hash_1 = "test hash"
hash_2 = 123
hash_3 = str([1, 2, 3])     # 集合
hash_4 = str(sorted({'A': 1}))
print("%s 的hash值为：%s" % (hash_1, hash(hash_1)))
print("%s 的hash值为：%s" % (hash_2, hash(hash_2)))
print("%s 的hash值为：%s" % (hash_3, hash(hash_3)))
print("%s 的hash值为：%s" % (hash_4, hash(hash_4)))
print("\n")
# --------------------------------
# hex() --- 将10进制整数转换成16进制，以字符串形式表示
print("hex的结果：", hex(255))
print("\n")
# --------------------------------
# bytearray()   --- 返回一个新自己数据，数组里的元素是可变的，并且每个元素的值的范围为 0 <= x < 256
print("bytearray....: ", bytearray([1, 2, 3]))
print("bytearray....: ", bytearray())
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
print("\n")
# ----------------------------------
# exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
exec('print("Hello World")')
print("\n")
# ----------------------------------
# str.format()  字符串格式化功能
print("{} {}".format("Hello", "Python"))
print("{1} {0} {1}".format("Hello", "Python"))
print("冲动的人：{name1}, 喜欢的人：{name2}".format(name1="小徐", name2="where?"))
print("\n")
# -----------------------------------
# compile(source, filename, mode[, flags[, dont_inherit]]) --- 将一个字符串编译为字节代码
#   source -- 字符串或者AST（Abstract Syntax Trees）对象
#   filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
#   mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
#   flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
#   flags和dont_inherit是用来控制编译源码时的标志
compile_str = "for i in range(10): print(i)"
c_str = compile(compile_str, '', 'exec')
print("编译后执行结果是：", exec(c_str))
print("\n")


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


# 12. issubclass(class, classinfo)  --- 判断参数class是否是类型参数classinfo的子类
class Issub_A:
    pass
class Issub_B(Issub_A):
    pass
print("%s 是否是 %s的之类？%s" % (Issub_B, Issub_A, issubclass(Issub_B, Issub_A)))
print("\n")
# -------------------------
# callable() --- 检查一个对象是否是可嗲用的，如果返回True，object仍有可能调用失败；如果返回False，调用绝对失败
print("callable 1返回：", callable(0))
print("callable 2返回：", callable(pow))
print("\n")
# -------------------------
# locals()  --- 以字典类型返回当前位置的全部局部变量
def return_local(x: object, y: object) -> object:
    z = 1
    print(locals())
all_result = return_local(2, 3)
print("返回当前位置的全部局部变量：", all_result)
print("\n")


# 13. super()   --- 函数是用于调用父类（超类）的方法
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
class Super_A(object):
    def add(self,x):
        y = x + 1
        print(y)
class Super_B(Super_A):
    def add(self,x):
        super().add(x)
superb = Super_B()
superb.add(2)
print("\n")
# ------------------------------
# property()    --- 在新式类中返回属性值
class Property_A(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
# -----------------------------------
# getattr() --- 返回一个对象属性值
class Getattr(object):
    bar = 1
g = Getattr()
print("获取属性值：", getattr(g, 'bar'))
print("\n")
# ------------------------------------
# delattr(object, name_of_atrr)
class Delattr(object):
    x = 1
    y = 2
    z = 3
d = Delattr()
print("d的属性：", d.x)
delattr(Delattr, 'x')
# print("d的属性：" % d.x)
print("\n")
# ------------------------------------
# setattr(object, name, value) -- 设置对象的属性值，该属性不一定是存在的
class Setattr(object):
    s1 = 1
s_1 = Setattr()
setattr(s_1, 's2', 5)
print("设置不存在属性的值：", s_1.s2)
print("\n")
# hasattr(object, name) --- 用于判断对象是否包含对应的属性
#   object--对象；name--属性名字符串
class Hasattr(object):
    x = 10
    y = 100
    z = 1000
print("判断对象是否含有属性：", hasattr(Hasattr, 'x'))
print("判断对象是否含有属性：", hasattr(Hasattr, 'e'))
print("\n")


# 14. filter(function, iterable)  --- 过滤序列中不符合条件的元素，返回由符合条件元素组成的新列表
#   function    --- 判断函数
#   iterable    --- 可迭代对象
def func_filter(x):
    list_a = []
    for i1 in x:
        if (i1 % 2) == 0:
           list_a.append(i1)
    return list_a
filter_result = func_filter([1, 2, 3, 4])
print("过滤后的序列为：%s" % filter_result)


# 15. len() --- 返回对象（字符、列表、元组等）长度或项目个数
len_1 = "len"
len_2 = [1, 2, 3, 4]
len_3 = (1, 2, 3)
print("%s 的长度为：%s" % (len_1, len(len_1)))
print("%s 的长度为：%s" % (len_2, len(len_2)))
print("%s 的长度为：%s" % (len_3, len(len_3)))
print("\n")
# vars()    --- 返回对象object的属性和属性值的字典对象。
class Vars_A(object):
    a = 1
print("vars()返回：", vars(Vars_A))
print("vars()返回：", vars(Vars_A()))
print("\n")
# -------------------------------------------------
# range(start, stop[, step])
range_result = range(10)
print("&&&&&&&&", range_result)
print("\n")
# -------------------------------------------------
# frozenset()   --- 返回一个冻结集合，冻结后结合不能再添加或删除任何元素
frozenset_1 = frozenset(range(10))
print("frozenset1: %s" % frozenset_1)
frozenset_2 = frozenset("HELLO")
print("frozenset2: %s" % frozenset_2)
print("\n")
# --------------------------------------------------
# globals() --- 以字典类型返回当前位置的全部变量
globals_1 = 'test'
print("当前位置的全局变量：", globals())
print("\n")


# 16.memoryview --- 返回给定参数的内存查看对象(Momory view)。
#   所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。
v = memoryview(bytearray('abc', 'utf-8'))
print(v[0])
print(v[1])
print(v[2])
print("\n")
# -------------------------
# round(x[, n]) --- 方法返回浮点数x的四舍五入值。
print(round(10.2565, 2))


# 17. help() --- 用于查看删除活模块的用途的详细说明
print(help('sys'))
print("\n")
# print(help('str'))
# --------------------------
# dir() --- 不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print("dir返回：", dir())
print("\n")
# id() --- 用于获取对象的内存地址
id_1 = '1'
id_2 = 1
id_3 = 4
print("%s 的内存id为：%s" % (id_1, id(id_1)))
print("%s 的内存id为：%s" % (id_2, id(id_2)))
print("%s 的内存id为：%s" % (id_3, id(id_3)))
print("\n")

