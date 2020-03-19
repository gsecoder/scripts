#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   conftest.py
@Time    :   2019/12/1017:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import pytest


@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
    output env config
    @return:
    @rtype:
    """
    # root_dir = request.config.rootdir
    # config_path = '{0}/config/env_config.yml'.format(root_dir)
    # with open(config_path) as f:
    #     # 读取配置文件
    #     env_config = yaml.load(f)
    # # 测试报告中展示host
    # allure.environment(host=env_config['host']['domain'])
    # # 测试报告中展示browser
    # allure.environment(browser=env_config['host']['browser'])
    # return env_config
    pass
