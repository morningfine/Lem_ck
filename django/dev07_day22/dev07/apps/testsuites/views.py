from rest_framework import viewsets
from rest_framework import permissions

from .models import Testsuits
from . import serializers


class TestsuitsViewSet(viewsets.ModelViewSet):

    queryset = Testsuits.objects.all()
    serializer_class = serializers.TestsuitModelSerializer
    permission_classes = [permissions.IsAuthenticated]

