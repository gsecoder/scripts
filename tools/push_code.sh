#!/usr/bin/env bash

# 查看当前的 git 分支并获取分支名称
current_branch_info=`git status | grep branch`
current_branch=${current_branch_info:10}

# 判断当前分支是否在 ${choice_branch} 分支上，如果不在的话进行分支的切换
if [ "${current_branch}" == "${choice_branch}" ]
then
  echo "当前分支为：${current_branch}"
else
  git checkout unittest_api
fi

# 提交代码
git add .
git commit -m "改造article query接口，开发接口查询自动化验证"
git push origin "${current_branch}"
