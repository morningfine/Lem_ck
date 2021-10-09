import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import mixins
from django.http.response import StreamingHttpResponse

from . import serializers
from .models import Reports
from utils.pagination import PageNumberPagination

logger = logging.getLogger('dev07')


class ReportViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Reports.objects.all()
    serializer_class = serializers.ReportsModelSerilizer
    permission_classes = [permissions.IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     for item in response.data['results']:
    #         item['result'] = '成功' if item.get('result') else '失败'
    #     return response

    def retrieve(self, request, *args, **kwargs):
        # TODO
        pass

    @action(detail=True)
    def download(self, request, *args, **kwargs):
        # 1、获取html源码
        # 2、将html源码转化为生成器对象
        # 3、
        response =  StreamingHttpResponse()
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f"attachment; filename*=UTF-8 '' {name + '.html'}"

