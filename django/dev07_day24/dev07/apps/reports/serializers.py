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

from .models import Reports


class ReportsModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ('update_time',)
        read_only_fields = ('name', 'count', 'result', 'success')
        extra_kwargs = {
            "create_time": {
                "read_only": True,
                "format": "%Y年%m月%d日 %H:%M:%S"
            },
            "name": {
                "read_only": True,
            },
            "html": {
                "write_only": True
            },
            "summary": {
                "write_only": True
            }

        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['result'] = '成功' if data.get('result') else '失败'
        return data
