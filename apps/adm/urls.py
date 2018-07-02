# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/8

from django.conf.urls import url

from adm import views_bsm, views_equipment

urlpatterns = [

    # 基础管理：供应商管理，品牌管理，资产类型管理
    url(r'supplier/$', views_bsm.SupplierView.as_view(), name="supplier"),
    url(r'supplier/list', views_bsm.SupplierListView.as_view(), name="supplier-list"),
    url(r'supplier/detail', views_bsm.SupplierDetailView.as_view(), name="supplier-detail"),
    url(r'supplier/delete', views_bsm.SupplierDeleteView.as_view(), name="supplier-delete"),

    url(r'assettype/$', views_bsm.AssetTypeView.as_view(), name="assettype"),
    url(r'assettype/list', views_bsm.AssetTypeListView.as_view(), name="assettype-list"),
    url(r'assettype/detail', views_bsm.AssetTypeDetailView.as_view(), name="assettype-detail"),
    url(r'assettype/delete', views_bsm.AssetTypeDeleteView.as_view(), name="assettype-delete"),

    url(r'customer/$', views_bsm.CustomerView.as_view(), name="customer"),
    url(r'customer/list', views_bsm.CustomerListView.as_view(), name="customer-list"),
    url(r'customer/detail', views_bsm.CustomerDetailView.as_view(), name="customer-detail"),
    url(r'customer/delete', views_bsm.CustomerDeleteView.as_view(), name="customer-delete"),

    url(r'equipmenttype/$', views_bsm.EquipmentTypeView.as_view(), name="equipmenttype"),
    url(r'equipmenttype/list', views_bsm.EquipmentTypeListView.as_view(), name="equipmenttype-list"),
    url(r'equipmenttype/detail', views_bsm.EquipmentTypeDetailView.as_view(), name="equipmenttype-detail"),
    url(r'equipmenttype/delete', views_bsm.EquipmentTypeDeleteView.as_view(), name="equipmenttype-delete"),

]
