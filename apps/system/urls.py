# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from system import views

urlpatterns = [
    # 系统工具
    url(r'^system_setup/$', views.SystemSetupView.as_view(), name="system_setup"),
    url(r'^email_setup/$', views.EmailSetupView.as_view(), name="email_setup"),
]
