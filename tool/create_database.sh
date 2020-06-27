#!/usr/bin/env bash

# 生成临时的迁移文件
python djangopy/manage.py makemigraions saas

# 在数据库中创建数据表
python djangopy/manage.py migrate saas




