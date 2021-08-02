from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import filters

from .models import Projects
from .serializers import ProjectSerilizer, ProjectModelSerializer


# class ProjectsView(View):
# class ProjectsView(APIView):
class ProjectsView(GenericAPIView):
    """
    继承GenericAPIView父类（GenericAPIView子类）
    a.具备View的所有特性
    b.具备了APIView中的认证、授权、限流功能
    c.还支持对于获取列表数据接口的功能：搜索、排序、分页
    """
    # 一旦继承GenericAPIView之后，往往需要指定queryset、serializer_class类属性
    # queryset指定当前类视图的实例方法需要使用的查询集对象
    queryset = Projects.objects.all()
    # serializer_class指定当前类视图的实例方法需要使用的序列化器类
    serializer_class = ProjectSerilizer

    # filter_backends在继承了GenericAPIView的类视图中指定使用的过滤引擎类（搜索、排序）
    # 优先级高于全局
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # 2、在继承了GenericAPIView的类视图中，search_fields类属性指定模型类中需要进行搜索过滤的字段名
    # 3、使用icontains查询类型作为过滤类型
    # 4、可以在字段名称前添加相应符号，指定查询类型
    #  '^': 'istartswith',
    #  '=': 'iexact',
    #  '$': 'iregex',
    search_fields = ['^name', '=leader', 'id']

    # ordering_fields类属性指定模型类中允许前端进行排序的字段名称
    # 前端默认可以使用ordering作为排序功能查询字符串参数名称，默认改字段的升序
    # 如果在字段名称前添加“-”，代表改字段降序
    # 如果指定多个排序字段，使用英文逗号进行分割
    ordering_fields = ['id', 'name', 'leader']

    def get(self, request: Request):
        # name_param = request.query_params.get('name')
        # if name_param:
        #     queryset = Projects.objects.filter(name__exact=name_param)
        # else:
        #     queryset = Projects.objects.all()

        # queryset = Projects.objects.all()

        # 1、在实例方法中，往往使用get_queryset()方法获取查询集对象
        # 2、一般不会指定调用queryset类属性，原因：为了提供让用户重写get_queryset()
        # 3、如果未重写get_queryset()方法，那么必须得指定queryset类属性
        # queryset = self.queryset
        # queryset = self.get_queryset()

        # filter_queryset对查询对象进行过滤操作
        queryset = self.filter_queryset(self.get_queryset())
        # serializer = ProjectSerilizer(instance=queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        # 1、在实例方法中，往往使用get_serializer()方法获取序列化器类
        # 2、一般不会直接调用serializer_class类属性，原因：为了让用户重写get_serializer_class()
        # 3、如果未重写get_serializer_class()方法，那么必须得指定serializer_class类属性
        # serializer = self.serializer_class(instance=queryset, many=True)
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # serializer = ProjectModelSerializer(data=request.data)
        # serializer = self.serializer_class(data=request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProjectsDetailView(APIView):
class ProjectsDetailView(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerilizer

    # a.lookup_url_kwarg默认为None
    # b.如果lookup_url_kwarg为None，那么lookup_url_kwarg与lookup_field值相同（‘pk’）
    # c.lookup_url_kwarg指定url路由条目中外键的路径参数名称，一般无需指定
    # lookup_url_kwarg = 'kk'

    # def get_object(self, pk):
    #     try:
    #         # project_obj = Projects.objects.get(id=pk)
    #         project_obj = self.get_queryset().get(id=pk)
    #         return project_obj
    #     except Exception as e:
    #         return Response({'msg': '参数有误'}, status=400)

    def get(self, request, **kwargs):
        # project_obj = self.get_object(pk)
        # get_object可以获取模型对象，无需传递外键值
        project_obj = self.get_object()

        # serializer = ProjectSerilizer(instance=project_obj)
        # serializer = self.serializer_class(instance=project_obj)
        serializer = self.get_serializer(instance=project_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        project_obj = self.get_object()

        serializer = self.get_serializer(instance=project_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # try:
        #     project_obj = Projects.objects.get(id=pk)
        # except Exception as e:
        #     return JsonResponse({'msg': '参数有误'}, status=400)
        project_obj = self.get_object()
        project_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
