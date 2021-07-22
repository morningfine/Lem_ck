import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Projects
# from projects.serializers import ProjectSerilizer
from .serializers import ProjectSerilizer


class ProjectsView(View):
    def get(self, request):
        # a.获取所有项目数据（查询集），获取列表数据
        queryset = Projects.objects.all()

        # b.将项目的查询集数据转化为嵌套字典的列表

        # 三、序列化器的使用
        # 1.可以使用序列化器进行序列化输出操作
        # a.创建序列化器对象
        # b.可以将模型对象或者查询集对象、普通对象、嵌套普通对象的列表，以instance关键字来传递参数
        # c.如果传递的是查询集对象、嵌套普通对象的列表（多条数据），必须得设置many=True
        # d.如果传递的是模型对象、普通对象，不需要设置many=True
        # e.可以使用序列化器对象的.data属性，获取序列化器之后的数据（字典、嵌套字典的列表）
        serializer = ProjectSerilizer(instance=queryset, many=True)

        # return JsonResponse(project_list, safe=False)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        # 1、获取json参数并转化为python中的数据类型（字典）
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 四、反序列化操作
        # 1.定义序列化器类，使用data关键字参数传递字典参数
        # 2.可以使用序列化器对象调用.is_valid()方法，才会开始对前端输入的参数进行校验
        # 3.如果校验通过.is_valid()方法返回True，否则返回False
        # 4.如果调用.is_valid()方法，添加raise_exeception=True，校验不通过会抛出异常，否则不会抛出异常
        # 5.只有在调用.is_valid()方法之后，才可以使用序列化器对象调用.errors属性，来获取错误提示信息（字典类型）
        # 6.只有在调用.is_valid()方法之后，才可以使用序列化器对象调用.validated_data属性，来获取校验通过之后的数据，
        # 与使用json.load转化之后的数据有区别
        serializer11 = ProjectSerilizer(data=python_data)

        if not serializer11.is_valid():
            return JsonResponse(serializer11.errors, status=400)

        # project_obj = Projects.objects.create(**python_data)
        project_obj = Projects.objects.create(**serializer11.validated_data)

        serializer = ProjectSerilizer(instance=project_obj)
        # return JsonResponse(python_dict, status=201)
        return JsonResponse(serializer.data, status=201)


class ProjectsDetailView(View):
    def get(self, request, pk):
        # 1、需要校验pk在数据库中是否存在

        # 2、从数据库中读取项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        serializer = ProjectSerilizer(instance=project_obj)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        # 1、需要校验pk在数据库中是否存在

        # 2、从数据库中读取项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 3、获取json参数并转化为python中的数据类型（字典）
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 需要进行大量的数据校验，且非常复杂
        serializer11 = ProjectSerilizer(data=python_data)

        if not serializer11.is_valid():
            return JsonResponse(serializer11.errors, status=400)

        # 4、更新数据
        project_obj.name = serializer11.validated_data.get('name')
        project_obj.leader = serializer11.validated_data.get('leader')
        project_obj.is_execute = serializer11.validated_data.get('is_execute')
        project_obj.desc = serializer11.validated_data.get('desc')
        project_obj.save()

        # 5、将读取的项目数据转化为字典
        serializer = ProjectSerilizer(instance=project_obj)
        # return JsonResponse(python_dict, status=201)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        # 1、需要校验pk在数据库中是否存在

        # 2、读取主键为pk的项目数据
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 3、执行删除
        project_obj.delete()

        return JsonResponse({'msg': '删除成功'}, status=204)
