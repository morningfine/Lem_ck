# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/2 21:32 
  @Auth : 可优
  @File : serializer.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterModelSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True
            },

        }

    def validate(self, attrs):
        pass

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data.get('username'),
                                        email=validated_data.get('username'))

        # 生成token
        user.token = 'xxxx'
        return user
