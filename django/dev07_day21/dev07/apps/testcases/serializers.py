import re
import json

from rest_framework import serializers

from interfaces.models import Interfaces
from .models import Testcases


class InterfaceProjectModelSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(label='所属的项目名称', help_text='所属的项目名称',
                                           slug_field='name', read_only=True)
    pid = serializers.IntegerField(label='所属项目id', help_text='所属项目id', write_only=True, validators=[])
    iid = serializers.IntegerField(label='所属接口id', help_text='所属接口id', write_only=True, validators=[])

    class Meta:
        model = Interfaces
        fields = ('name', 'project', 'pid', 'iid')
        extra_kwargs = {
            'name': {
                'read_only': True
            }
        }

    def validate(self, attrs):
        # TODO
        return attrs


class TestcaseModelSerializer(serializers.ModelSerializer):
    interface = InterfaceProjectModelSerializer(label='所属项目和接口信息', help_text='所属项目和接口信息')

    class Meta:
        model = Testcases
        exclude = ('create_time', 'update_time')
        extra_kwargs = {
            'request': {
                'write_only': True
            },
            'include': {
                'write_only': True
            },
        }

    def validate_request(self, attr):
        # TODO
        return attr

    def validate(self, attrs):
        # TODO
        return attrs

    def to_internal_value(self, data):
        result = super().to_internal_value(data)
        # TODO
        pass

    # def create(self, validated_data):
    #     pass
