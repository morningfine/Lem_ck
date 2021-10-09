# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/18 21:42 
  @Auth : 可优
  @File : common.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
import os
import json

import yaml

from testcases.models import Testcases
from envs.models import Envs
from debugtalks.models import DebugTalks
from configures.models import Configures


def generate_testcase_file(instance: Testcases, env: Envs, testcase_dir_path: str):
    # 3、创建以项目名命名的目录
    project_name = instance.interface.project.name
    testcase_dir_path = os.path.join(testcase_dir_path, project_name)
    if not os.path.exists(testcase_dir_path):
        os.makedirs(testcase_dir_path)
        debugtalk_obj = DebugTalks.objects.filter(project__name=project_name).first()
        # 生成debugtalks.py
        with open(os.path.join(testcase_dir_path, 'debugtalk.py'), 'w', encoding='utf-8') as file:
            file.write(debugtalk_obj.debugtalk)

    # 获取当前用例的接口名称，创建以接口命名的路径
    interface_name = instance.interface.name
    testcase_dir_path = os.path.join(testcase_dir_path, interface_name)
    if not os.path.exists(testcase_dir_path):
        os.makedirs(testcase_dir_path)

    # 4、yaml用例文件
    testcase_list = []
    # 获取config数据
    include_data = json.loads(instance.include, encoding='utf-8')
    config_id = include_data.get('config')
    base_url = env.base_url if env.base_url else ''

    if config_id is not None:
        config_obj = Configures.objects.filter(id=config_id).first()
        config_dict = json.loads(config_obj.request, encoding='utf-8')
        config_dict['config']['request']['base_url'] = base_url
    else:
        config_dict = {
            'config': {
                'name': instance.name,
                'request': {
                    'base_url': base_url
                }
            }
        }

    testcase_list.append(config_dict)

    # 获取前置用例id列表
    testcase_id_list = include_data.get('testcases')

    if testcase_id_list:
        for testcase_id in testcase_id_list:
            # TODO
            pass

    with open('xxx.yaml', 'w', encoding='utf-8') as one_file:
        yaml.dump(testcase_list, one_file)