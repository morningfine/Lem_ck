from rest_framework import viewsets
from rest_framework import permissions

from .models import Testcases
from . import serializers


class TestcasesViewSet(viewsets.ModelViewSet):

    queryset = Testcases.objects.all()
    serializer_class = serializers.TestcaseModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        intance = self.get_object() # type: Testcases
        # TODO
        data = {
            "author": intance.author,
            "testcase_name": "这是一个演示用例",
            "selected_configure_id": 1,
            "selected_interface_id": 1,
            "selected_project_id": 1,
            "selected_testcase_id": [1,2,3],
            "method": "POST",
            "url": "/user/login/",
            "param": [ ],
            "header": [
                {
                "key": "uname",
                "value": "keyou"
                },
                {
                "key": "age",
                "value": "18"
                }
            ],
            "variable": [ ],
            "jsonVariable": "",
            "extract": [
                {
                    "key": "username",
                    "value": "content.username"
                },
                {
                    "key": "myAge",
                    "value": "content.age"
                }
            ],
            "validate": [
                {
                    "key": "status_code",
                    "value": 200,
                    "comparator": "equals",
                    "param_type": "int"
                },
                {
                    "key": "love",
                    "value": "lemon",
                    "comparator": "equals",
                    "param_type": "string"
                }
            ],
            "globalVar": [
                {
                    "key": "var1",
                    "value": "val1",
                    "param_type": "string"
                },
                {
                    "key": "var2",
                    "value": 100,
                    "param_type": "int"
                }
            ],
            "parameterized": [
                {
                    "key": "name-age",
                    "value": '[["name":"keyou","age":18],["name":"lemon","age":19],["name":"youyou","age":20]]'
                },
                {
                    "key": "n-a",
                    "value": "${getname()}"
                }
            ],
            "setupHooks": [
                {
                    "key": "sh1"
                },
                {
                    "key": "sh2"
                }
            ],
            "teardownHooks": [
                {
                    "key": "th1"
                },
                {
                    "key": "th2"
                }
            ]
        }

        return Response(data)
