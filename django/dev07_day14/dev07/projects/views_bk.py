from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import filters

from .models import Projects
from .serializers import ProjectSerilizer, ProjectModelSerializer
from utils.pagination import PageNumberPagination


# Mixin拓展类
class ListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # 3、调用paginate_queryset方法对查询集对象进行分页
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(instance=page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateModelMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ProjectsView(GenericAPIView):
class ProjectsView(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=name', '=leader', '=id']
    ordering_fields = ['id', 'name', 'leader']

    # 可以在类视图中指定分页引擎类，优先级高于全局
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # # 3、调用paginate_queryset方法对查询集对象进行分页
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(instance=page, many=True)
        #     return self.get_paginated_response(serializer.data)
        # serializer = self.get_serializer(instance=queryset, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

        # a.python中支持多重继承，一个类可以同时继承多个父类
        # b.类中的方法和属性是按照__mro__所指定的继承顺序进行搜索
        # print(ProjectsView.__mro__)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return self.create(request, *args, **kwargs)


class ProjectsDetailView(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerilizer

    def get(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
