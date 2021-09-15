import logging

from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions

from .models import Projects
from .serializers import ProjectModelSerializer,ProjectsNamesModelSerailizer
from utils.pagination import PageNumberPagination


logger = logging.getLogger('dev07')


class ProjectViewSet(viewsets.ModelViewSet):
    """
    list:
    获取项目列表数据

    retrieve:
    获取项目详情数据

    update:
    更新项目信息

    names:
    获取项目名称

    """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=name', '=leader', '=id']
    ordering_fields = ['id', 'name', 'leader']

    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # result_list = []
        for item in response.data['results']:
            # TODO
            item['interfaces'] = 3
            item['testsuits'] = 3
            item['testcases'] = 3
            item['configures'] = 3
            # result_list.append(item)

        # response.data['results'] = result_list
        return response

    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        logger.info(response.data)
        return response

    @action(detail=True)
    def interfaces(self, request, *args, **kwargs):
        # TODO
        project = self.get_object()
        interfaces_qs = project.interfaces_set.all()
        interfaces_data = [{'id': interface.id, 'name': interface.name} for interface in interfaces_qs]

        # logger.debug(interfaces_data)
        return Response(interfaces_data, status=200)

    def get_serializer_class(self):
        """
        a.可以重写父类的get_serializer_class方法，用于为不同的action提供不一样的序列化器类
        b.在视图集对象中可以使用action属性获取当前访问的action方法名称
        :return:
        """
        if self.action == 'names':
            return ProjectsNamesModelSerailizer
        else:
            # return self.serializer_class
            return super().get_serializer_class()

    def paginate_queryset(self, queryset):
        if self.action == "names":
            return
        else:
            return super().paginate_queryset(queryset)

    def get_queryset(self):
        if self.action == "names":
            return self.queryset.filter(name__icontains='2')
        else:
            return super().get_queryset()

