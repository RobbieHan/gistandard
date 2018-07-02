# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from rbac import views_role, views_menu

urlpatterns = [

    # 组织架构的改删查操作
    url(r'^role/$', views_role.RoleView.as_view(), name="role"),
    url(r'^role/list$', views_role.RoleListView.as_view(), name="role-list"),
    url(r'^role/detail$', views_role.RoleDetailView.as_view(), name="role-detail"),
    url(r'^role/delete$', views_role.RoleDeleteView.as_view(), name="role-delete"),
    url(r'^role/role_menu$', views_role.Role2MenuView.as_view(), name="role-role_menu"),
    url(r'^role/role_menu_list$', views_role.Role2MenuListView.as_view(), name="role-role_menu_list"),
    url(r'^role/role_user$', views_role.Role2UserView.as_view(), name="role-role_user"),

    # 菜单管理
    url(r'^menu/$', views_menu.MenuView.as_view(), name="menu"),
    url(r'^menu/list$', views_menu.MenuListView.as_view(), name="menu-list"),
    url(r'^menu/detail$', views_menu.MenuListDetailView.as_view(), name="menu-detail"),
]
