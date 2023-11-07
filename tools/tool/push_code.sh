#!/usr/bin/env bash

# 查看当前分支并获取分支的名称
current_branch_info=$(git status | grep branch)
current_branch=${current_branch_info:10}

# 判断当前分支是否在 ${current_branch} 分支上，如果不在的话进行分支切换
if [ "${current_branch}" == "${choice_current}" ]; then
  echo "当前分支为：${current_branch}"
  esle
  git switch master
fi

# 提交代码
git add .
git commit -m "发送短信验证码注册"
git push origin "${current_branch}"
