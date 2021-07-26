import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Projects
# from projects.serializers import ProjectSerilizer
from .serializers import ProjectSerilizer


class ProjectsView(View):
    def get(self, request):
        queryset = Projects.objects.all()
        serializer = ProjectSerilizer(instance=queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        serializer11 = ProjectSerilizer(data=python_data)
        if not serializer11.is_valid():
            return JsonResponse(serializer11.errors, status=400)

        # project_obj = Projects.objects.create(**serializer11.validated_data)
        # 1、如果在创建序列化器对象时，仅传递data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的create方法
        # 2、create方法用于对数据进行创建操作
        # 3、序列化器类中的create方法，validated_data参数为校验通过之后的数据（一般字典类型）
        # 4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data字典中
        # 5、create方法一般需要将创建成功之后模型对象返回
        serializer11.save(myname='珍惜', myage=18)

        # serializer = ProjectSerilizer(instance=project_obj)
        # return JsonResponse(serializer.data, status=201)

        # 1、在创建序列化器对象时，仅仅只传递data参数，那么必须得调用is_valid()方法通过之后
        # 2、如果没有调用save方法，使用创建序列化器对象.data属性，来获取序列化输出的数据
        #   （会把validated_data数据作为输入源，参照序列化器字段的定义来进行输入）
        # 3、如果调用了save方法，使用创建序列化器对象.data属性，来获取序列化输出的数据
        #   （会把create方法返回的模型对象数据作为输入源，参照序列化器字段的定义来进行输出）
        return JsonResponse(serializer11.data, status=201)


class ProjectsDetailView(View):
    def get(self, request, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        serializer = ProjectSerilizer(instance=project_obj)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        try:
            python_data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # serializer11 = ProjectSerilizer(data=python_data)
        serializer = ProjectSerilizer(instance=project_obj, data=python_data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        # 4、更新数据
        # project_obj.name = serializer11.validated_data.get('name')
        # project_obj.leader = serializer11.validated_data.get('leader')
        # project_obj.is_execute = serializer11.validated_data.get('is_execute')
        # project_obj.desc = serializer11.validated_data.get('desc')
        # project_obj.save()

        # 1、如果在创建序列化器对象时，同时instance和data参数，使用序列化器对象调用save方法时，会自动调用序列化器类中的update方法
        # 2、update方法用于对数据进行更新操作
        # 3、序列化器类中的update方法，instance参数为待更新的模型对象，validated_data参数为校验通过之后的数据（一般字典类型）
        # 4、在调用save方法时，可以传递任意的关键字参数，并且会自动合并到validated_data字典中
        # 5、update方法一般需要将更新成功之后模型对象返回
        serializer.save()

        # 5、将读取的项目数据转化为字典
        # serializer = ProjectSerilizer(instance=project_obj)
        return JsonResponse(serializer.data, status=201)

    def delete(self, request, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 3、执行删除
        project_obj.delete()

        return JsonResponse({'msg': '删除成功'}, status=204)
