# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/4/26 21:37 
  @Auth : 可优
  @File : urls.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'interfaces', views.InterfaceViewSet)

urlpatterns = [
]

urlpatterns += router.urls
