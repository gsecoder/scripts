#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   conftest.py
@Time    :   2019/12/919:24
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest
import allure
import yaml

@pytest.fixture(scope="function")
def login():
    print("登录成功")
    
    
@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    output env config
    @return:
    @rtype:
    """
    root_dir = request.config.rootdir
    config_path = '{0}/config/env_config.yml'.format(root_dir)
    with open(config_path) as f:
        # 读取配置文件
        env_config = yaml.load(f)
    
    return env_config

