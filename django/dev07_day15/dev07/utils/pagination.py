# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2021/5/26 20:19 
  @Auth : 可优
  @File : pagination.py
  @IDE  : PyCharm
  @Motto: ABC(Always Be Coding)
  @Email: keyou100@qq.com
  @Company: 湖南省零檬信息技术有限公司
  @Copyright: 柠檬班
-------------------------------------------------
"""
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination


class PageNumberPagination(_PageNumberPagination):
    # 指定默认每一页显示3条数据
    page_size = 3

    # 前端用于指定页码的查询字符串参数名称
    page_query_param = 'pp'
    # 前端用于指定页码的查询字符串参数描述
    page_query_description = '获取的页码'

    # 前端用于指定每一页显示的数据条数，查询字符串参数名称
    page_size_query_param = 'ss'
    page_size_query_description = '每一页数据条数'

    max_page_size = 50
    invalid_page_message = '无效页码'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_num'] = self.page.number
        response.data['max_num'] = self.page.paginator.num_pages
        return response

