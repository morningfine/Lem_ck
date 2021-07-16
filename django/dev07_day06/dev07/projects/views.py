import json

from django.db.models import Q, manager, QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import connection

# from projects.models import Projects
from .models import Projects
from interfaces.models import Interfaces

# 在views.py中定义的函数，称为视图函数
from django.views import View


def index(request):
    return HttpResponse("欢迎测试开发7期的大佬们！")


# def get_project(request):
#     return HttpResponse("<h1>这是一个项目信息</h1>")
#
#
# def get_project1(request):
#     return HttpResponse("<h1>这是项目1的信息</h1>")
#
#
# def get_project2(request):
#     return HttpResponse("<h1>这是项目2的信息</h1>")


# def get_project(request):
#     return HttpResponse("<h1>获取项目信息</h1>")
#
#
# def create_project(request):
#     return HttpResponse("<h1>创建项目信息</h1>")
#
#
# def put_project(request):
#     return HttpResponse("<h1>更新项目信息</h1>")
#
#
# def delete_project(request):
#     return HttpResponse("<h1>删除项目信息</h1>")
#
#
# def get_projects(request, pk):
#     return HttpResponse(f"<h1>获取项目{pk}信息</h1>")


def projects(request):
    """
    视图函数
    a.视图函数的第一参数是HttpRequest对象
    b.HttpRequest对象包含了请求的所有数据（请求头、请求体）
    c.视图函数必须得返回一个HttpResponse对象或者其子类对象
    :param request:
    :return:
    """
    # print(request)
    # print(type(request))
    # print(type(request).__mro__)
    if request.method == 'GET':
        #
        #
        #
        return HttpResponse("<h1>获取项目信息</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>创建项目信息</h1>")
    elif request.method == 'PUT':
        return HttpResponse("<h1>更新项目信息</h1>")
    elif request.method == 'DELETE':
        return HttpResponse("<h1>删除项目信息</h1>")
    else:
        return HttpResponse("<h1>其他操作</h1>")


class ProjectsView(View):
    """
    一、定义类视图
    1.继承View或者View子类
    2.不通的请求方法有相应的方法进行对应
        GET   ->   get
        POST  ->   post
        PUT   ->   put
        DELETE ->  delete
        PATCH  -> patch
    3.每一个处理请求的方法，必须得返回HttpResponse对象或者HttpResponse子类对象
    4.每一个处理请求的方法，第二个参数必须为HttpRequest对象
    """

    def get(self, request, pk):
        # 一、创建（C）
        # 方式一：
        # a.直接使用模型类(字段名1=值1, 字段名2=值2, ...)，来创建模型类实例
        # b.必须模型实例调用save()方法，才会执行sql语句
        # obj = Projects(name='xxx金融项目', leader='多喝热水')
        # obj.save()

        # 方式二：
        # a.使用模型类.objects返回manager对象
        # b.使用manager对象.create(字段名1=值1, 字段名2=值2, ...)，来创建模型类实例
        # c.无需使用模型实例调用save()方法，会自动执行sql语句
        # obj = Projects.objects.create(name='xxx22', leader='lemon')

        # 二、读取（R）
        # 1、读取多条数据
        # 读取数据库中所有数据
        # a.使用模型类.objects.all()，会将当前模型类对应的数据表中的所有数据读取出来
        # b.模型类.objects.all()，返回QuerySet对象（查询集对象）
        # c.QuerySet对象，类似于列表，具有惰性查询的特性（在‘用’数据时，才会执行sql语句）
        # qs = Projects.objects.all()

        # 2、读取单条数据
        # 方式一：
        # a.可以使用模型类.objects.get(条件1=值1)
        # b.如果使用指定条件查询的记录数量为0，会抛出异常
        # c.如果使用指定条件查询的记录数量超过1，也会抛出异常
        # d.最好使用具有唯一约束的条件去查询
        # e.如果使用指定条件查询的记录数量为1，会返回这条记录对应的模型实例对象，可以使用模型对象.字段名去获取相应的字段值
        # obj = Projects.objects.get(id=1)

        # 方式二：
        # a.可以使用模型类.objects.filter(条件1=值1)，返回QuerySet对象
        # b.如果使用指定条件查询的记录数量为0，会返回空的QuerySet对象
        # c.如果使用指定条件查询的记录数量超过1，将符合条件的模型对象包裹到QuerySet对象中返回
        # d.QuerySet对象，类似于列表，有如下特性：
        # 1）支持通过数值（正整数）索引取值
        # 2）支持切片操作（正整数）
        # 3）获取第一个模型对象：QuerySet对象.first()
        # 4）获取最后一个模型对象：QuerySet对象.last()
        # 5）获取长度：len(QuerySet对象)、QuerySet对象.count()
        # 6）判断查询集是否为空：QuerySet对象.exists()
        # 7）支持迭代操作（for循环，每次循环返回模型对象）

        # e.ORM框架中，会给每一个模型类中的主键设置一个别名（pk）
        # qs = Projects.objects.filter(id=1)
        # qs = Projects.objects.filter(pk=1)
        # Projects.objects.filter(id__gt=1)

        # filter方法支持多种查询类型
        # 1）字段名__查询类型=具体值
        # 2）字段名__exact=具体值，缩写形式为：字段名=具体值
        # 3）字段名__gt：大于、字段名__gte：大于等于
        # 4）字段名__lt：小于、字段名_lte：小于等于
        # 5）contains：包含
        # 6）startswith：以xxx开头
        # 7）endswith：以xxx结尾
        # 8）isnull：是否为null
        # 9）一般在查询类型前添加“i”，代表忽略大小写

        # exclude为反向查询，filter方法支持的所有查询类型，都支持

        # 创建从表数据
        # 外键对应的父表如何传递？
        # 方式一：
        # 1）先获取父表模型对象
        # 2）将获取的父表模型对象以外键字段名作为参数来传递
        # project_obj = Projects.objects.get(name='在线图书项目')
        # interface_obj = Interfaces.objects.create(name='在线图书项目-登录接口', tester='珍惜',
        #                                           projects=project_obj)

        # 方式二：
        # 1）先获取父表模型对象，进而获取父表数据的id值
        # 2）将父表数据的主键id值以外键名_id作为参数来传递
        # interface_obj = Interfaces.objects.create(name='在线图书项目-注册接口', tester='珍惜',
        #                                           projects_id=project_obj.id)

        # a.通过从表模型对象（已经获取到了），如何获取父表数据？
        #   可以通过外键字段先获取父表模型对象
        #   interface_obj.projects，返回父表模型对象
        # interface_obj = Interfaces.objects.get(id=1)

        # b.通过父表模型对象（已经获取到了），如何获取从表数据？
        #   默认可以通过从表模型类名小写_set，返回manager对象，可以进一步使用filter进行过滤
        #   如果在从表模型类的外键字段指定了related_name参数，那么会使用related_name指定参数作为名称
        #   project_obj.interfaces_set.all()
        # project_obj = Projects.objects.get(id=1)
        # project_obj.interfaces_set.all()

        # c.如果想要通过父表参数来获取从表数据、想要通过从表参数获取父表数据  --- 关联查询
        # 可以使用关联查询语句：
        # 关联字段名称__关联模型类中的字段名称__查询类型
        # Interfaces.objects.filter(projects__name__contains='xxx')
        # Projects.objects.filter(interfaces__name__contains='登录')

        # d.逻辑关系
        # 与关系
        # 方式一：
        #   在同一个filter方法内部，添加多个关键字参数，那么每个条件为“与”的关系
        # 方式二：
        #   可以多次调用filter方法，那么filter方法的条件为“与”的关系  --- QuerySet链式调用特性
        # qs = Projects.objects.filter(name__contains='2', leader='keyou')

        # 或关系
        #   可以使用Q查询，实现逻辑关系，多个Q对象之间如果使用“|”，那么为“或”关系
        # qs = Projects.objects.filter(Q(name__contains='2') | Q(leader='多喝热水'))

        # e.排序（QuerySet）
        #   可以使用QuerySet对象（manager对象）.order_by('字段名1', '字段名2', '-字段名3')
        #   默认为ASC升序，可以在字段名称前添加“-”，那么为DESC降序
        # Projects.objects.filter(Q(name__contains='2') | Q(leader='多喝热水')).order_by('-name', 'leader')

        # 三、更新（U）
        # 方式一：一条数据
        # project_obj = Projects.objects.get(id=1)
        # project_obj.name = '在线图书项目（一期）'
        # project_obj.leader = '不语'
        # 1）必须调用save方法才会执行sql语句，并且默认进行完整更新
        # 2）可以在save方法中设置update_fields参数（序列类型），指定需要更新的字段名称（字符串）
        # project_obj.save()

        # 方式二：多条数据
        # Projects.objects.filter: QuerySet
        # 可以在QuerySet对象.update(字段名称='字段值')，返回修改成功的值，无需调用save方法
        # qs = Projects.objects.filter(name__contains='2').update(leader='珍惜')
        # interface_obj.projects.name

        # 四、删除（D）
        # 方式一：一条数据
        project_obj = Projects.objects.get(id=1)
        project_obj.delete()

        # 方式二：多条数据
        # obj = Projects.objects.filter(name__contains='2').delete()

        # return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii': False}, status=201, safe=False)
        # return JsonResponse(project_data_list, json_dumps_params={'ensure_ascii': False}, status=201, safe=False)

    def post(self, request, pk):
        # 前端参数解析
        # 前端传递参数的方式
        # 1.路径参数
        #   a.在url路径中传递的参数
        #   b.在请求实例方法中，使用关键字参数来接收

        # 2.查询字符串参数
        #   a.url ？后面的key value键值对参数，如：http://www.xxx.com/?key1=value1&key2=value2
        #   b.request.GET获取
        #   c.request.GET返回QueryDict，类似于python中dict类型
        #   d.可以使用['key1']、get('key1')，会返回具体的值，如果有多个相同key的键值对，获取的是最后一个
        #   e.getlist('key1')，获取相同key的多个值，返回list类型

        # 请求体参数
        # 1.json
        #   a.json格式的参数会存放在body中，一般为字节类型
        #   b.json.loads(request.body)，返回Python中的数据类型（字典、嵌套字典的列表）
        # json.loads(request.body)

        # 2.www-form-urlencoded
        #   a.一般在前端页面中使用表单录入的参数
        #   b.request.POST返回QueryDict，类似于python中dict类型

        # 3.file（multipart/data）
        #   a.传递的文本参数可以使用request.POST去提取
        #   b.传递的非文本参数（二进制文件）可以使用request.FILES去提取
        #   c.如果传递纯粹的文件，request.body去提取

        # 请求头参数
        #   a.第一种方式：request.headers['key1']或者.get('key1')
        #   b.第二种方式：request.META['HTTP_AUTHORIZATION']
        #       1）请求头参数的可以被转化为：HTTP_参数名大写
        #       2）如果参数名中含有-，会自动转换为_
        return HttpResponse("<h1>创建项目信息</h1>")

    def put(self, request):
        return HttpResponse("<h1>更新项目信息</h1>")

    def delete(self, request):
        return HttpResponse("<h1>删除项目信息</h1>")
