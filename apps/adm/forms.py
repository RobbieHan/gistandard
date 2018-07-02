# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/20

from django import forms
from .models import Supplier, AssetType, Customer, EquipmentType, Equipment, Asset, AssetFile


class SupplierCreateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        error_messages = {
            "company": {"required": "请输入分销商公司名称"},
            "address": {"required": "请输入分销商公司地址"},
            "linkname": {"required": "请输入分销商联系人"},
            "phone": {"required": "请输入分销商联系电话"}
        }

    def clean(self):
        cleaned_data = super(SupplierCreateForm, self).clean()
        company = cleaned_data.get("company")
        if Supplier.objects.filter(company=company).count():
            raise forms.ValidationError('分销商："{}"已存在'.format(company))


class SupplierUpdateForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        error_messages = {
            "company": {"required": "请输入分销商公司名称"},
            "address": {"required": "请输入分销商公司地址"},
            "linkname": {"required": "请输入分销商联系人"},
            "phone": {"required": "请输入分销商联系电话"}
        }


class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = '__all__'


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['unit', 'address', 'name', 'phone', 'status', 'belongs_to', 'desc']
        error_messages = {
            "unit": {"required": "请填写客户单位"},
            "address": {"required": "请填写客户单位地址"},
            "name": {"required": "请填写客户联系人"},
            "phone": {"required": "请填写客户联系电话"}
        }

    def clean(self):
        cleaned_data = super(CustomerCreateForm, self).clean()
        unit = cleaned_data.get("unit")
        if Customer.objects.filter(unit=unit).count():
            raise forms.ValidationError('客户单位："{}"已经存在'.format(unit))


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['unit', 'address', 'name', 'phone', 'status', 'belongs_to', 'desc']
        error_messages = {
            "unit": {"required": "请填写客户单位"},
            "address": {"required": "请填写客户单位地址"},
            "name": {"required": "请填写客户联系人"},
            "phone": {"required": "请填写客户联系电话"}
        }


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentCreateForm(forms.ModelForm):

    class Meta:
        model = Equipment
        fields = '__all__'
        error_messages = {
            "number": {"required": "设备编号不能为空"},
            "equipment_model": {"required": "请输入设备型号"},
            "buy_date": {"required": "请输入购买日期"},
            "warranty_date": {"required": "请输入质保日期"},
            "supplier": {"required": "请选择分销商"}
        }

    def clean(self):
        cleaned_data = super(EquipmentCreateForm, self).clean()
        number = cleaned_data.get("number")
        if Equipment.objects.filter(number=number).count():
            raise forms.ValidationError('设备编号：{}已存在'.format(number))


class EquipmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Equipment
        # fields = '__all__'
        # 排除 service_info字段，不然通过modelform更新数据时，m2m数据会丢失
        exclude = ['service_info', ]
        error_messages = {
            "number": {"required": "设备编号不能为空"},
            "equipment_model": {"required": "请输入设备型号"},
            "buy_date": {"required": "请输入购买日期"},
            "warranty_date": {"required": "请输入质保日期"},
            "supplier": {"required": "请选择分销商"}
        }


class AssetCreateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        error_messages = {
            "assetNum": {"required": "资产编号不能为空"},
            "model": {"required": "请输入资产型号"},
            "buyDate": {"required": "请输入购买日期"},
            "warrantyDate": {"required": "请输入质保日期"},
            "status": {"required": "请选择资产状态"}
        }

    def clean(self):
        cleaned_data = super(AssetCreateForm, self).clean()
        number = cleaned_data.get("assetNum")
        if Asset.objects.filter(assetNum=number).count():

            raise forms.ValidationError('资产编号：{}已存在'.format(number))

class AssetUpdateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        error_messages = {
            "assetNum": {"required": "资产编号不能为空"},
            "model": {"required": "请输入资产型号"},
            "buyDate": {"required": "请输入购买日期"},
            "warrantyDate": {"required": "请输入质保日期"},
            "status": {"required": "请选择资产状态"}
        }


class AssetUploadForm(forms.ModelForm):
    class Meta:
        model = AssetFile
        fields = '__all__'
