# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/5/14 20:21 
  @Auth : 可优
  @File : serializers.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from interfaces.models import Interfaces
from .models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        exclude = ('update_time', )
        extra_kwargs = {
            "create_time": {
                "read_only": True,
                # TODO
                "format": "xxxx"
            }
        }

    def create(self, validated_data):
        # TODO
        # 创建debugtalk数据
        pass



class ProjectsNamesModelSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('id', 'name')
