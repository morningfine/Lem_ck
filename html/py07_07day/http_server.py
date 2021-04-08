"""
============================
author:MuSen
time:2019/6/21
E-mail:3247119728@qq.com
============================
"""

from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)

#  测试数据
user_info = {"user": 'python01', 'pwd': 'lemonban'}

project_data = {"code": "1",
                "data": [{"title": "前程贷", "id": "1001"},
                         {"title": "智慧金融", "id": "1002"},
                         {"title": "生鲜到家", "id": "1003"},
                         {"title": "柠檬班app", "id": "1004"}],
                "msg": "四个项目",
                }
# 接口数据
interface_data = {
    "1001": {"code": "1",
             "data": [{"name": "前程贷登录1001"},
                      {"name": "前程贷注册1001"}],
             "msg": "2个接口", },

    "1002": {"code": "1",
             "data": [{"name": "智慧-登录1002"},
                      {"name": "智慧-注册1002"},
                      {"name": "智慧-贷款1004"}, ],
             "msg": "3个接口", },

    "1003": {"code": "1",
             "data": [{"name": "生鲜-登录1003"},
                      {"name": "生鲜-注册1003"},
                      {"name": "生鲜下单1003"}, ],
             "msg": "3个接口", },

    "1004": {"code": "1",
             "data": [{"name": "app登录1004"},
                      {"name": "app注册1004"},
                      {"name": "app报名1004"},
                      {"name": "app缴费1004"},
                      ],
             "msg": "4个接口", },
}


# 登录
@app.route('/api/user/login', methods=['post'])
def login():
    """
    接口地址：http://127.0.0.1:5000/api/user/login
    请求方法：post
    参数： {user:账号,pwd:密码}
    参数类型：表单 、json都支持
    返回:该项目的所有接口
    """
    data = request.form or request.json
    # 判断账号，密码是否正确
    if user_info.get('user') == data.get('user') and user_info.get('pwd') == data.get('pwd'):
        return jsonify({'code': "1", "data": None, "msg": "成功"})
    else:
        return jsonify({'code': "0", "data": None, "msg": "密码有误"})


# 获取项目列表
@app.route('/api/projects', methods=['get'])
def pro_list():
    """
    接口地址：http://127.0.0.1:5000/api/projects
    请求方法：get
    参数：无
    返回所有的项目
    :return:
    """
    return jsonify(project_data)


# 获取接口列表
@app.route('/api/interface', methods=['get'])
def interface():
    """
    接口地址：http://127.0.0.1:5000/api/interface
    请求方法：get
    参数： id(项目的id)
    参数类型：查询字符串
    返回:该项目的所有接口

    """
    inter_id = request.args.get('id')

    if inter_id:
        res_data = interface_data.get(inter_id)
        if res_data:
            return jsonify(res_data)
        else:
            return jsonify({"code": "0", "data": None, "msg": "没有该项目"})
    else:
        return jsonify({"code": "0", "data": None, "msg": "请求参数不能为空"})


if __name__ == '__main__':
    cors = CORS(app)
    app.run(debug=True)