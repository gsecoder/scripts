#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   32_text_xml.py
@Time    :   2019/12/2214:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import sys

import os
from xml.dom.minidom import parse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


class OperateXml(object):
    
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = "../OperateFile/data/xml.xml"
        
        self.dom = self.read_xml()
    
    def read_xml(self):
        """
        :return: 获取xml文件对象
        """
        dom = parse(self.file_name)
        return dom
    
    def get_document_element(self):
        """
        :return: rootNode---获取跟元素对象
        :return: 获取文档根元素
        """
        rootNode = self.dom.documentElement
        return rootNode.nodeName
    
    def get_root_next_info(self):
        """
        :return:
        """
        rootNode = self.dom.documentElement
        persons = rootNode.getElementsByTagName("person")
        for person in persons:
            if person.hasAttribute("ID"):
                print("ID: %s" % person.getAttribute("ID"))
                # id 参数
                id = person.getElementsByTagName("id")[0]
                print(id.nodeName, ":", id.childNodes[0].data)
                # name 参数
                name = person.getElementsByTagName("name")[0]
                print(name.nodeName, ":", name.childNodes[0].data)
                # sex 参数
                sex = person.getElementsByTagName("sex")[0]
                print(sex.nodeName, ":", sex.childNodes[0].data)
                # comments 参数---xml不解析
                comments = person.getElementsByTagName("comments")[0]
                print(comments.nodeName, ":", comments.childNodes[0].data)
            else:
                print("......")
    
    def write_xml(self):
        # 获取文档根元素
        rootNode = self.dom.documentElement
        
        # 新建一个person节点
        person_node = self.dom.createElement("person")
        person_node.setAttribute("ID", "p004")
        
        # 创建id节点，并设置textValue
        id_node = self.dom.createElement("id")
        id_text_value = self.dom.createTextNode("4")
        # 把文本节点挂到id_node节点上，即赋予值
        id_node.appendChild(id_text_value)
        # 把id_node挂在到person节点上，认亲
        person_node.appendChild(id_node)
        
        # 创建name节点，并设置textValue
        name_node = self.dom.createElement("name")
        name_text_value = self.dom.createTextNode("D")
        # 把文本节点挂到name_node节点上，即赋予值
        name_node.appendChild(name_text_value)
        # 把name_node挂在到person节点上，认亲
        person_node.appendChild(name_node)
        
        # 创建age节点，并设置textValue
        age_node = self.dom.createElement("age")
        age_text_value = self.dom.createTextNode("23")
        # 把文本节点挂到age_node节点上，即赋予值
        age_node.appendChild(age_text_value)
        # 把age_node挂在到person节点上，认亲
        person_node.appendChild(age_node)
        
        # 创建sex节点，并设置textValue
        sex_node = self.dom.createElement("sex")
        sex_text_value = self.dom.createTextNode("male")
        # 把文本节点挂到sex_node节点上，即赋予值
        sex_node.appendChild(sex_text_value)
        # 把sex_node挂在到person节点上，认亲
        person_node.appendChild(sex_node)
        
        # 创建comments节点，并设置textValue
        comments_node = self.dom.createElement("comments")
        comments_text_value = self.dom.createCDATASection("create success")
        # 把文本节点挂到comments_node节点上，即赋予值
        comments_node.appendChild(comments_text_value)
        # 把comments_node挂在到person节点上，认亲
        person_node.appendChild(comments_node)
        
        # 将上面创建的子节点挂在到根节点
        rootNode.appendChild(person_node)
        
        # 调整格式
        with open(self.file_name, 'w') as f:
            self.dom.writexml(f, addindent="", encoding="utf-8")
    
    def update_xml(self):
        # 文档根元素
        rootNode = self.dom.documentElement
        
        # 找到自己要更新的节点
        persons = rootNode.getElementsByTagName("person")
        for person in persons:
            name = person.getElementsByTagName("name")[0]
            # print(name.childNodes[0].data)
            if name.childNodes[0].data == "A1":
                # 获取到name节点的父节点
                pn = name.parentNode
                print("pn: %s" % pn)
                # 父节点的age节点，就是name的兄弟节点
                age = pn.getElementsByTagName("age")[0]
                print("age: %s" % age)
                # 更新想要更新节点的值
                name.childNodes[0].data = "A11"
                age.childNodes[0].data = "9999"
            else:
                print("请检查你的节点是否存在")
        
        with open(self.file_name, 'w') as f:
            self.dom.writexml(f, addindent='', encoding="utf-8")


if __name__ == "__main__":
    ox = OperateXml()
    print("获取xml文件对象：%s" % ox.read_xml())
    print("获取文档根元素: %s" % ox.get_document_element())
    # 获取xml各个节点信息
    # ox.get_root_next_info()
    # 向xml文件中写数据
    # ox.write_xml()
    # 更新xml文件数据
    ox.update_xml()
