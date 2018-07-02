# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/11/10

import re

from django.utils.deprecation import MiddlewareMixin

class MenuMiddleware(MiddlewareMixin):
    """
    获取菜单：获取用户权限信息，根具用户访问的URL来处理子菜单数据
    """

    def get_menu(self, request):
        """
        获取用户权限菜单：这个地方真的好乱，没有更好的实现方法只能先忍受下吧
        :param request:
        :return:
        """
        if request.user.is_authenticated():
            user = request.user
            permissions_item_list = user.roles.values('permissions__id',
                                                      'permissions__title',
                                                      'permissions__url',
                                                      'permissions__icon',
                                                      'permissions__code',
                                                      'permissions__parent').distinct()
            permission_url_list = []
            permission_menu_list = []

            for item in permissions_item_list:
                permission_url_list.append(item['permissions__url'])
                if item['permissions__id']:
                    menu = {
                        'id': item['permissions__id'],
                        'title': item['permissions__title'],
                        'url': item['permissions__url'],
                        'icon': item['permissions__icon'],
                        'code': item['permissions__code'],
                        'parent': item['permissions__parent'],
                        'status': False,
                        'sub_menu': [],

                    }
                    permission_menu_list.append(menu)

            request_url = request.path_info
            top_menu = []
            permission_menu_dict = {}
            for menu in permission_menu_list:
                url = menu['url']
                if url and re.match(url, request_url):
                    menu['status'] = True
                if menu['parent'] is None:
                    top_menu.insert(0, menu)
                permission_menu_dict[menu['id']] = menu

            menu_data = []
            for i in permission_menu_dict:
                if permission_menu_dict[i]['parent']:
                    pid = permission_menu_dict[i]['parent']
                    parent_menu = permission_menu_dict[pid]
                    parent_menu['sub_menu'].append(permission_menu_dict[i])
                else:
                    menu_data.append(permission_menu_dict[i])

            if [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url]:
                reveal_menu = [menu['sub_menu'] for menu in menu_data if menu['url'] in request_url][0]
            else:
                reveal_menu = None

            return top_menu, reveal_menu, permission_url_list
        else:
            pass

    def process_request(self, request):
        if self.get_menu(request):
            request.top_menu, request.reveal_menu, request.permission_url_list = self.get_menu(request)

