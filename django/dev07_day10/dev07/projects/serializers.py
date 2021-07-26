# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/5/14 20:21 
  @Auth : 可优
  @File : serializers.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from interfaces.models import Interfaces
from .models import Projects


# 1、自定义的序列化器类实际上也是Field的子类
# 2、所以自定义的序列化器类可以作为另一个序列化器中的字段来使用
class InterfaceSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    tester = serializers.CharField()


# 1、可以在类外自定义校验函数
# 2、第一个参数为待校验的值
# 3、如果校验不通过，必须得抛出serializers.ValidationError('报错信息')异常，同时可以指定具体的报错信息
# 4、需要将校验函数名放置到validators列表中
def is_contains_keyword(value):
    if '项目' not in value:
        raise serializers.ValidationError('项目名称中必须得包含“项目”关键字')


class ProjectSerilizer(serializers.Serializer):
    """
    二、定义序列化器类
    1.必须得继承Serializer类或者Serializer子类
    2.定义的序列化器类中，字段名要与模型类中的字段名保持一致
    3.定义的序列化器类的字段（类属性）为Field子类
    4.默认定义哪些字段，那么哪些字段就会返回前端，同时也必须的输入（前端需要传递）
    5.常用的序列化器字段类型
        IntegerField  -> int
        CharField     -> str
        BooleanField  -> bool
        DateTimeField -> datetime
    6.可以在序列化器字段中指定不同的选项
        label和help_text，与模型类中的verbose_name和help_text参数一样
        IntegerField，可以使用max_value指定最大值，min_value指定最小值
        CharField，可以使用max_length指定最大长度，min_length指定最小长度

    7.定义的序列化器字段中，required默认为True，说明默认定义的字段必须得输入和输出
    8.如果在序列化器字段中，设置required=False，那么前端用户可以不传递该字段（校验时会忽略改该字段，所以不会报错）
    9.如果未定义模型类中的某个字段，那么该字段不会输入，也不会输出
    10.前端必须的输入（反序列化输入）name（必须得校验），但是不会需要输出（序列化器输出）？
        如果某个参数指定了write_only=True，那么该字段仅仅只输入（反序列化输入，做数据校验），不会输出（序列化器输出），
        默认write_only为False
    11.前端可以不用传递，但是后端需要输出？
        如果某个参数指定了read_only=True，那么该字段仅仅只输出（序列化器输出），不会输入（反序列化输入，做数据校验），
        默认read_only为False
    12.在序列化器类中定义的字段，默认allow_null=False，该字段不允许传递null空值，
        如果指定allow_null=True，那么该字段允许传递null
    13.在序列化器类中定义CharField字段，默认allow_blank=False，该字段不允许传递空字符串，
        如果指定allow_blank=True，那么该字段允许传递空字符串
    14.在序列化器类中定义的字段，可以使用default参数来指定默认值，如果指定了default参数，那么前端用户可以不用传递，
        会将default指定的值作为入参
    """
    # id = serializers.IntegerField(label='项目id', help_text='项目id', max_value=1000, min_value=1)
    # name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5, write_only=True)
    # name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5, read_only=True)

    # 1、可以在序列化器字段上使用validators指定自定义的校验规则
    # 2、validators必须得为序列类型（列表），在列表中可以添加多个校验规则
    # 3、DRF框架自带UniqueValidator校验器，必须得使用queryset指定查询集对象，用于对该字段进行校验
    # 4、UniqueValidator校验器，可以使用message指定自定义报错信息
    # 5、校验规则的执行顺序？
    #   对字段类型进行校验 -> 依次验证validators列表中的校验规则 -> 从右到左依次验证其他规则 -> 调用单字段校验方法
    #   -> 调用多字段联合校验方法validate方法
    name = serializers.CharField(label='项目名称', help_text='项目名称', max_length=20, min_length=5,
                                 error_messages={
                                     'min_length': '项目名称不能少于5位',
                                     'max_length': '项目名称不能超过20位'
                                 }, validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名称不能重复'),
                                                is_contains_keyword])
    # leader = serializers.CharField(label='项目负责人', help_text='项目负责人', allow_null=True)
    # leader = serializers.CharField(label='项目负责人', help_text='项目负责人', allow_blank=True)
    leader = serializers.CharField(label='项目负责人', help_text='项目负责人', default='阿名')
    is_execute = serializers.BooleanField(write_only=True)

    # 1、如果定义了一个模型类中没有的字段，并且该字段需要输出（序列化输出）
    # 2、需要在create方法、update方法中的模型对象上，添加动态的属性即可
    # token = serializers.CharField(read_only=True)

    # 3、如果定义了一个模型类中没有的字段，并且该字段需要输入（反序列化输入）
    # 4、需要在create方法、update方法调用之前，将该字段pop调用
    # sms_code = serializers.CharField(write_only=True)

    # a.DateTimeField可以使用format参数指定格式化字符串
    # b.可以任意序列化器字段上使用error_messages来自定义错误提示信息
    # c.使用校验选项名（校验方法名）作为key，把具体的错误提示信息作为value
    # update_time = serializers.DateTimeField(label='更新时间', help_text='更新时间', format='%Y年%m月%d日 %H:%M:%S',
    #                                         error_messages={'required': '该字段为必传参数'})

    # 一、关联字段
    # 1、可以定义PrimaryKeyRelatedField来获取关联表的外键值
    # 2、如果通过父获取从表数据，默认需要使用从表模型类名小写_set作为序列化器类中的关联字段名称
    # 3、如果在定义模型类的外键字段时，指定了realated_name参数，那么会把realated_name参数名作为序列化器类中的关联字段名称
    # 4、PrimaryKeyRelatedField字段，要么指定read_only=True，要么指定queryset参数，否则会报错
    # 5、如果指定了read_only=True，那么该字段仅序列化输出
    # 6、如果指定了queryset参数（关联表的查询集对象），用于对参数进行校验
    # 7、如果关联字段有多个值，那么必须添加many=True，一般父表获取从表数据时，关联字段需要指定
    # interfaces_set = serializers.PrimaryKeyRelatedField(label='项目所属接口id', help_text='项目所属接口id',
    #                                                     many=True, queryset=Interfaces.objects.all(), write_only=True)

    # 1、使用StringRelatedField字段，将关联字段模型类中的__str__方法的返回值作为该字段的值
    # 2、StringRelatedField字段默认添加了read_only=True，该字段仅序列化输出
    # interfaces_set = serializers.StringRelatedField(many=True)

    # 1、使用SlugRelatedField字段，将关联模型类中的某个字段，作为该字段的值
    # 2、如果指定了read_only=True，那么该字段仅序列化输出
    # 3、如果该字段需要进行反序列化输入，那么必须得指定queryset参数，同时关联字段必须有唯一约束
    # interfaces_set = serializers.SlugRelatedField(slug_field='name', many=True, queryset=Interfaces.objects.all())

    # interfaces_set = InterfaceSerilizer(label='所属接口信息', help_text='所属接口信息', read_only=True,
    #                                     many=True)

    # 1、可以在序列化器类中对单个字段进行校验
    # 2、单字段的校验方法名称，必须把validate_作为前缀，加上待校验的字段名，如：validate_待校验的字段名
    # 3、如果校验不通过，必须得返回serializers.ValidationError('具体报错信息')异常
    # 4、如果校验通过，往往需要将校验之后的值，返回
    # 5、如果该字段在定义时添加的校验规则不通过，那么是不会调用单字段的校验方法
    def validate_name(self, attr: str):
        if not attr.endswith('项目'):
            raise serializers.ValidationError('项目名称必须得以“项目”结尾')
        return attr

    # 1、可以在序列化器类中对多个字段进行联合校验
    # 2、使用固定的validate方法，会接收上面校验通过之后的字典数据
    # 3、当所有字段定义时添加的校验规则都通过，且每个字段的单字段校验方法通过的情况下，才会调用validate
    def validate(self, attrs: dict):
        if len(attrs.get('leader')) <= 4 or not attrs.get('is_execute'):
            raise serializers.ValidationError('项目负责人名称长度不能少于4位或者is_execute参数为False')
        return attrs

    # def to_internal_value(self, data):
    #     # 1、to_internal_value方法，是所有字段开始进行校验时入口方法（最先调用的方法）
    #     # 2、会依次对序列化器类的各个序列化器字段进行校验：
    #     #   对字段类型进行校验 -> 依次验证validators列表中的校验规则 -> 从右到左依次验证其他规则 -> 调用单字段校验方法
    #     #    to_internal_value调用结束 -> 调用多字段联合校验方法validate方法
    #     tmp = super().to_internal_value(data)
    #     # 对各个单字段校验结束之后的数据进行修改
    #     return tmp

    # def to_representation(self, instance):
    #     # 1、to_representation方法，是所有字段开始进行序列化输出时的入口方法（最先调用的方法）
    #     tmp =super().to_representation(instance)
    #     return tmp

    def create(self, validated_data: dict):
        myname = validated_data.pop('myname')
        myage = validated_data.pop('myage')
        validated_data.pop('sms_code')
        project_obj = Projects.objects.create(**validated_data)
        project_obj.token = 'xxxxxxxxxxxxx'
        return project_obj

    def update(self, instance, validated_data: dict):
        # for key, value in validated_data.items():
        #     setattr(instance, key, value)
        instance.name = validated_data.get('name') or instance.name
        instance.leader = validated_data.get('leader') or instance.leader
        instance.is_execute = validated_data.get('is_execute') or instance.is_execute
        instance.desc = validated_data.get('desc') or instance.desc
        instance.save()
        return instance


class ProjectModelSerializer(serializers.ModelSerializer):
    """
    定义模型序列化器类
    1、继承serializers.ModelSerializer类或者其子类
    2、需要在Meta内部类中指定model、fields、exclude类属性参数
    3、model指定模型类（需要生成序列化器的模型类）
    4、fields指定模型类中哪些字段需要自动生成序列化器字段
    5、会给id主键、指定了auto_now_add或者auto_now参数的DateTimeField字段，添加read_only=True，仅仅只进行序列化输出
    6、有设置unique=True的模型字段，会自动在validators列表中添加唯一约束校验<UniqueValidator
    7、有设置default=True的模型字段，会自动添加required=False
    8、有设置null=True的模型字段，会自动添加allow_null=True
    9、有设置blank=True的模型字段，会自动添加allow_blank=True
    """
    class Meta:
        model = Projects
        # fields指定模型类中哪些字段需要自动生成序列化器字段
        # a.如果指定为"__all__"，那么模型类中所有的字段都需要自动转化为序列化器字段
        # b.可以传递需要转化为序列化器字段的模型字段名元组
        fields = "__all__"
        # fields = ('id', 'name', 'leader')
        # c.exclude指定模型类中哪些字段不需要转化为序列化器字段，其他的字段都需要转化
        # exclude = ('create_time', 'update_time')
