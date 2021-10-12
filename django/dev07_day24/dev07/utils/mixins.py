# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/6/16 20:07 
  @Auth : 可优
  @File : mixins.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework.decorators import action


class NamesMixin:
    @action(methods=['GET'], detail=False)
    def names(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        # logger.info(response.data)
        return response

    def paginate_queryset(self, queryset):
        """
        names action禁用分页功能
        :param queryset:
        :return:
        """
        if self.action == "names":
            return
        else:
            return super().paginate_queryset(queryset)

    def filter_queryset(self, queryset):
        """
        names action禁用过滤功能
        :param queryset:
        :return:
        """
        if self.action == "names":
            return self.queryset
        else:
            return super().filter_queryset(queryset)


class RunMixin:

    def execute(self, qs):
        # 1、取出用例模型对象并获取env_id
        instance = self.get_object()  # type: Testcases
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        env_id = serializer.validated_data.get('env_id')
        env = Envs.objects.get(id=env_id)

        # 2、创建以时间戳命名的目录
        # dirname = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        testcase_dir_path = os.path.join(settings.PROJECT_DIR, datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        os.makedirs(testcase_dir_path)

        for obj in qs:
            # 3、创建以项目名命名的目录
            # 4、生成debugtalks.py、yaml用例文件
            common.generate_testcase_file(obj, env, testcase_dir_path)

        # 5、运行用例并生成测试报告
        return common.run_testcase(instance, testcase_dir_path)
