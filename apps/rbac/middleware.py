# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/18

import re

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class RbacMiddleware(MiddlewareMixin):
    """
    检查用户URL访问权限
    """

    def process_request(self, request):
        if hasattr(request, 'permission_url_list'):
            request_url = request.path_info
            permission_url = request.permission_url_list
            for url in settings.SAFE_URL:
                if re.match(url, request_url):
                    return None
            if request_url in permission_url:
                return None
            else:
                ret = dict(url=[url for url in permission_url if url is not None])
                ret['request_url'] = request_url
                return render(request, 'page404.html', ret)
