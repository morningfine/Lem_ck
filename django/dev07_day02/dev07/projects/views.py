from django.http import HttpResponse
from django.shortcuts import render


# 在views.py中定义的函数，称为视图函数
def index(request):
    return HttpResponse("欢迎测试开发7期的大佬们！")


# def get_project(request):
#     return HttpResponse("<h1>这是一个项目信息</h1>")
#
#
# def get_project1(request):
#     return HttpResponse("<h1>这是项目1的信息</h1>")
#
#
# def get_project2(request):
#     return HttpResponse("<h1>这是项目2的信息</h1>")


def get_project(request):
    return HttpResponse("<h1>获取项目信息</h1>")


def create_project(request):
    return HttpResponse("<h1>创建项目信息</h1>")


def put_project(request):
    return HttpResponse("<h1>更新项目信息</h1>")


def delete_project(request):
    return HttpResponse("<h1>删除项目信息</h1>")


def get_projects(request, pk):
    return HttpResponse(f"<h1>获取项目{pk}信息</h1>")
