# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/16 20:07 
  @Auth : 可优
  @File : mixins.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework.decorators import action


class NamesMixin:
    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # logger.info(response.data)
        return response

    def paginate_queryset(self, queryset):
        """
        names action禁用分页功能
        :param queryset:
        :return:
        """
        if self.action == "names":
            return
        else:
            return super().paginate_queryset(queryset)

    def filter_queryset(self, queryset):
        """
        names action禁用过滤功能
        :param queryset:
        :return:
        """
        if self.action == "names":
            return self.queryset
        else:
            return super().filter_queryset(queryset)
