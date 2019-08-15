#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   31_fileOperate.py
@Time    :   2019/7/22 10:52
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# here put the import lib
# 1. 文件读取
# codecs模块：主要用来解决文件乱码的问题
import codecs

f_read = codecs.open('read_file.txt', 'rb', encoding="utf-8")
text = f_read.read()
print(type(text))
print("f_read: ", text)
f_read.close()


# 2. 写文件
f_write = codecs.open('write_file.txt', 'wb', encoding='utf-8')
f_write.write("********************\n")
f_write.write("<鹅>\n")
f_write.write("鹅，鹅，鹅\n")
f_write.write("曲项向天歌\n")
f_write.write("白毛浮绿水\n")
f_write.write("红掌拨清波\n")
f_write.close()


# 3.文件操作的常用方法
# 3.1 readlines()：用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。
f_readlines = codecs.open('write_file.txt', 'rb', encoding='utf-8')
text_list = f_readlines.readlines()
print('text_list_type: ', type(text_list))
print("text_list: ", text_list)
print(text_list[2])
f_readlines.close()

# 3.2 readline()：用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
#     __next__()：返回迭代器的下一个指向
f_readline = codecs.open('read_file.txt', 'rb', encoding='utf-8')
readline_list = f_readline.readline()
print('readline_list_type: ', type(readline_list))
print("readline_list: ", readline_list)
print(f_readline.__next__())
print(f_readline.__next__())
f_readline.close()

# 3.3 writelines()：用于向文件中写入一序列的字符串。
f_writelines = codecs.open("writelines_file.txt", 'wb', encoding='utf-8')
write_list = f_writelines.write("1213311\nnewbanlance\n\n")
writelines_list = f_writelines.writelines(["11111111\n", '2222222\n', '333333333\n'])
f_writelines.close()

# 3.4 tell()：返回文件的当前位置，即文件指针当前位置。
f_tell = codecs.open('tell_file.txt', 'wb', encoding='utf-8')
f_tell.write("1213311\nnewbanlance\n\n")
print(f_tell.tell())
f_tell.writelines(["11111111\n", '2222222\n', '333333333\n'])
print(f_tell.tell())
f_tell.close()

# 3.5 seek()：用于移动文件读取指针到指定位置
f_seek = codecs.open('seek_file.txt', 'wb', encoding='utf-8')
f_seek.write("abcdefgh\n12131313\n\djkfdjskfjkd\n")
print(f_seek.tell())
f_seek.seek(0)
f_seek.writelines(["11111111\n", '2222222\n', '333333333\n'])
f_seek.close()

# 3.6 name(): 读取文件名
f_name = codecs.open('name_file.txt', 'wb', encoding='utf-8')
print("f_name： ", f_name.name)
print("f_name_closed", f_name.closed)

# 3.7 flush(): 刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。一般情况下，文件关闭后会自动刷新缓冲区，
# 但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。


# 4.Python文件上下文管理
with codecs.open('with_file.txt', 'wb', encoding='utf-8') as f_with:
    f_with.write("test with.")
    print("f_with_closed: ", f_with.closed)
print("f_with_closed: ", f_with.closed)
