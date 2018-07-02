# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from users import views_user, views_structure

urlpatterns = [
    # 用户增改删查操作
    url(r'^user/$', views_user.UserView.as_view(), name="user"),
    url(r'^user/list$', views_user.UserListView.as_view(), name="user-list"),
    url(r'^user/detail$', views_user.UserDetailView.as_view(), name="user-detail"),
    url(r'^user/update$', views_user.UserUpdataView.as_view(), name="user-update"),
    url(r'^user/create$', views_user.UserCreateView.as_view(), name="user-create"),
    url(r'^user/delete$', views_user.UserDeleteView.as_view(), name="user-delete"),
    url(r'^user/enable$', views_user.UserEnableView.as_view(), name="user-enable"),
    url(r'^user/disable$', views_user.UserDisableView.as_view(), name="user-disable"),
    url(r'^user/adminpasswdchange$', views_user.AdminPasswdChangeView.as_view(), name="user-adminpasswdchange"),

    # 组织架构的改删查操作
    url(r'^structure/$', views_structure.StructureView.as_view(), name="structure"),
    url(r'^structure/list$', views_structure.StructureListView.as_view(), name="structure-list"),
    url(r'^structure/detail$', views_structure.StructureDetailView.as_view(), name="structure-detail"),
    url(r'^structure/delete$', views_structure.StructureDeleteView.as_view(), name="structure-delete"),
    url(r'^structure/add_user$', views_structure.Structure2UserView.as_view(), name="structure-add_user"),
]
