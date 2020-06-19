#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__   : sorting_express.py
__author__ : jiangheng
__function__:
    将 source.txt 文件数据源里的快递信息进行分拣，最终生成的数据格式如下
{
"北京市":[
    ['王*龙', '北京市海淀区苏州街大恒科技大厦南座4层'],
    ['庞*飞', '北京市昌平区汇德商厦四楼403'],
    ....
],
"山东省":[
    ['孙*云', '山东省济南市山东省济南市历下区祥泰汇东国际，一号楼3005室'],
    ['鞠*龙', '山东省潍坊市玉清街江山帝景B区12号楼一单元14楼'],
    ['张*', '山东省济南市兴港路三庆城市主人']
....
],
...
....
}
"""
import json


def sorting_express():

    provinces = [
        '北京', '上海', '天津', '重庆',
        '河北', '山西', '内蒙古',
        '辽宁', '吉林', '黑龙江',
        '江苏', '浙江', '安徽', '福建', '江西', '山东',
        '河南', '湖北', '湖南', '广东', '广西', '海南',
        '重庆', '四川', '贵州', '云南', '西藏',
        '陕西', '甘肃', '青海', '宁夏', '新疆',
        '香港', '澳门', '台湾'
    ]

    with open('source.txt', 'r', encoding='utf-8') as f:
        # 读取快递地址文件数据
        source_data = f.readlines()
        # print("source_data", source_data)
        temp_dict = {}
        # 枚举要分类的省
        for province in enumerate(provinces):
            # 遍历源数据
            for i, val in enumerate(source_data):
                if 1 < i < len(source_data) - 2:
                    # print(type(source_data))

                    # 获取每一条数据的地址信息，并做格式处理，并判断每条数据的对应的省份是什么
                    province_name = province[1]
                    # print("......: ", province_name)
                    format_val = val.split(',')[1].lstrip(" '").startswith(province_name)
                    if format_val:
                        str_val = val.lstrip('\t').rstrip('\n').rstrip(',')
                        if province_name not in temp_dict:
                            temp_dict[province_name] = []
                            temp_dict[province_name].append(str_val)
                        else:
                            temp_dict[province_name].append(str_val)
        print(json.dumps(
            temp_dict,
            indent=4,
            ensure_ascii=False
        ))


if __name__ == "__main__":
    sorting_express()