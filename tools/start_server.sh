#!/usr/bin/env bash

# 查看当前的工作路径，如果不在工作路劲则进行切换
echo "当前工作路径为：`pwd`"

# 查看当前的 git 分支并获取分支名称
current_branch_info=`git status | grep branch`
current_branch=${current_branch_info:10}

# 定义要操作的分支
choice_branch='unittest_api'

# 判断当前分支是否在 ${choice_branch} 分支上，如果不在的话进行分支的切换
if [ "${current_branch}" == "${choice_branch}" ]
then
  echo "当前分支为：${current_branch}"
else
  git checkout mock_django_api
fi

# 激活当前项目的虚拟环境
source env/Scripts/activate

# 由于执行激活虚拟环境命令没有输出相应的信息
# 可以通过查看环境中安装的第三方库来判断是否激活了虚拟环境，如果是环境所用的包则证明激活了
pip list

# 启动项目服务
python mock_django_api/manage.py runserver 127.0.0.1:8000