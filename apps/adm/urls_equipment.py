# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from adm import views_equipment

urlpatterns = [

    url(r'^$', views_equipment.EquipmentView.as_view(), name='equipment'),
    url(r'^list', views_equipment.EquipmentListView.as_view(), name="list"),
    url(r'^create', views_equipment.EquipmentCreateView.as_view(), name="create"),
    url(r'^detail', views_equipment.EquipmentDetailView.as_view(), name="equipment-detail"),
    url(r'^delete', views_equipment.EquipmentDeleteView.as_view(), name='delete'),
    url(r'^serviceinfoupdate', views_equipment.ServiceInfoUpdateView.as_view(), name='service-info-update'),
]
