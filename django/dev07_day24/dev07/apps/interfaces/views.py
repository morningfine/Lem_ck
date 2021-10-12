import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions

from .models import Interfaces
from . import serializers
from utils.pagination import PageNumberPagination
from testcases.models import Testcases
from configures.models import Configures


logger = logging.getLogger('dev07')


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for item in response.data['results']:
            item['testcases'] = Testcases.objects.filter(interface_id=item.get('id')).count()
            item['configures'] = Configures.objects.filter(interface_id=item.get('id')).count()
        return response

    @action(detail=True)
    def testcases(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data = response.data.get('testcases_set')
        return response

    @action(detail=True)
    def configures(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response.data = response.data.get('configures')
        return response

    def get_serializer_class(self):
        if self.action == 'testcases':
            return serializers.TestcasesInterfacesModelSerializer
        elif self.action == 'configures':
            return serializers.ConfiguresInterfacesModelSerializer
        else:
            return super().get_serializer_class()
