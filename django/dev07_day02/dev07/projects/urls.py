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
from django.urls import path

# from projects.views import get_project, create_project, put_project, delete_project
# from projects import views
from . import views

urlpatterns = [
    path('get/', views.get_project),
    path('create/', views.create_project),
    path('put/', views.put_project),
    path('delete/', views.delete_project),
    path('a/', views.delete_project)
]

