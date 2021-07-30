import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Projects
from .serializers import ProjectSerilizer, ProjectModelSerializer


# class ProjectsView(View):
class ProjectsView(APIView):
    """
    继承APIView父类（Django中View的子类）
    a.具备View的所有特性
    b.提供了认证、授权、限流功能
    """
    def get(self, request):
        queryset = Projects.objects.all()
        serializer = ProjectSerilizer(instance=queryset, many=True)
        # return JsonResponse(serializer.data, safe=False)

        # 在DRF中Response为HTTPResponse的子类
        # a.data参数为序列化之后的数据（一般为字典或嵌套字典的列表）
        # b.会自动根据渲染器来将数据转化为请求头中Accept需要的格式进行返回
        # c.status指定响应状态码
        # d.content_type指定响应头中的Content-Type，一般无需指定，会根据渲染器来自动设置
        return Response(serializer.data, status=status.HTTP_200_OK, content_type='ap')

    def post(self, request):
        # a.一旦继承APIView之后，request是DRF中Request对象
        # b.Request是在HttpRequest基础上做了拓展
        # c.兼容HttpRequest的所有功能
        # d.前端传递的查询字符串参数：GET、query_params
        # e.前端传递application/json、application/x-www-form-urlencoded、multipart/form-data参数
        #   可以根据请求头中Content-Type，使用统一的data属性获取
        # try:
        #     python_data = json.loads(request.body)
        # except Exception as e:
        #     return JsonResponse({'msg': '参数有误'}, status=400)

        # python_data = request.data
        serializer = ProjectModelSerializer(data=request.data)
        # if not serializer.is_valid():
        #     # return JsonResponse(serializer11.errors, status=400)
        #     return Response(serializer.errors, status=400)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectsDetailView(APIView):
    def get(self, request, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        serializer = ProjectSerilizer(instance=project_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
            return project_obj
        except Exception as e:
            return Response({'msg': '参数有误'}, status=400)

    def put(self, request, pk):
        # try:
        #     project_obj = Projects.objects.get(id=pk)
        # except Exception as e:
        #     return JsonResponse({'msg': '参数有误'}, status=400)
        project_obj = self.get_object(pk)

        serializer = ProjectSerilizer(instance=project_obj, data=request.data)

        # if not serializer.is_valid():
        #     return JsonResponse(serializer.errors, status=400)
        # 在序列化器对象调用is_valid(raise_exception=True)，校验失败时，会抛出异常，DRF框架会自动处理异常
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        try:
            project_obj = Projects.objects.get(id=pk)
        except Exception as e:
            return JsonResponse({'msg': '参数有误'}, status=400)

        # 3、执行删除
        project_obj.delete()

        # return JsonResponse({'msg': '删除成功'}, status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)
