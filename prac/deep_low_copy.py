#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : deep_low_copy.py
__time__    : 2020/6/23 9:08
__author__  : 
__github__  : https://github.com/crisimple/  
__resume__  : None
"""

import copy

list_sample = [1, 2, 3, [4, 5]]
list_copy = copy.copy(list_sample)
print("list_sample: ", list_sample)
print("list_copy: ", list_copy)
print("list_samp_id: ", id(list_sample))
print("list_copy_id: ", id(list_copy))
print("list_samp_id: ", id(list_sample[3]))
print("list_copy_id: ", id(list_copy[3]))

list_sample.append(6)
list_copy.append(66)
print("list_sample2", list_sample)
print("list_copy2", list_copy)

list_sample[3].append(6)
list_copy[3].append(66)
print("list_sample3", list_sample)
print("list_copy3", list_copy)

# list_sample = [1, 2, 3, [4, 5]]
# list_copy = copy.deepcopy(list_sample)
# print("list_sample", list_sample)
# print("list_copy", list_copy)
#
# list_sample.append(6)
# list_copy.append(66)
# print("list_sample2", list_sample)
# print("list_copy2", list_copy)
#
# list_sample[3].append(6)
# list_copy[3].append(66)
# print("list_sample3", list_sample)
# print("list_copy3", list_copy)
