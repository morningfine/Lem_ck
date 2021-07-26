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

from .models import Interfaces



class InterfacesSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    tester = serializers.CharField()

    projects = serializers.PrimaryKeyRelatedField()
