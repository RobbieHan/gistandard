import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model
from django.db.models import Q

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Supplier, AssetType, Customer, EquipmentType
from .forms import SupplierCreateForm, SupplierUpdateForm, AssetTypeForm, CustomerCreateForm, CustomerUpdateForm, \
    EquipmentTypeForm

User = get_user_model()

class SupplierView(LoginRequiredMixin, View):
    """
    供应商管理
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/supplier.html', ret)


class SupplierListView(LoginRequiredMixin, View):
    """
    获取分销商列表
    """
    def get(self, request):
        filters = dict()
        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(Supplier.objects.values().filter(**filters)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class SupplierDetailView(LoginRequiredMixin, View):
    """
    分销商详情页：查看、修改、新建数据
    """
    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            supplier = get_object_or_404(Supplier, pk=request.GET.get('id'))
            ret['supplier'] = supplier
        users = User.objects.exclude(id=request.user.id)
        ret['users'] = users
        return render(request, 'adm/bsm/supplier_detail.html', ret)

    def post(self, request):
        # res = dict(result=False)
        # if 'id' in request.POST and request.POST['id']:
        #     supplier = get_object_or_404(Supplier, pk=request.POST.get('id'))
        # else:
        #     supplier = Supplier()
        # supplier_form = SupplierForm(request.POST, instance=supplier)
        # if supplier_form.is_valid():
        #     supplier_form.save()
        #     res['result'] = True
        # return HttpResponse(json.dumps(res), content_type='application/json')
        res = {}
        if 'id' in request.POST and request.POST['id']:
            supplier = get_object_or_404(Supplier, pk=request.POST.get('id'))
            supplier_update_form = SupplierUpdateForm(request.POST, instance=supplier)
            if supplier_update_form.is_valid():
                supplier_update_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(supplier_update_form.errors)
                supplier_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'supplier_form_errors': supplier_form_errors[0]
                }

        else:
            supplier = Supplier()
            supplier_create_form = SupplierCreateForm(request.POST, instance=supplier)
            if supplier_create_form.is_valid():
                supplier_create_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(supplier_create_form.errors)
                supplier_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'supplier_form_errors': supplier_form_errors[0]
                }
        return HttpResponse(json.dumps(res), content_type='application/json')



class SupplierDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Supplier.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AssetTypeView(LoginRequiredMixin, View):
    """
    资产类型
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/assettype.html', ret)


class AssetTypeListView(LoginRequiredMixin, View):
    """
    资产类型列表
    """
    def get(self, request):
        fields = ['id', 'name', 'desc']
        ret = dict(data=list(AssetType.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AssetTypeDetailView(LoginRequiredMixin, View):
    """
    资产类型：查看、修改、新建数据
    """
    def get(self, request):
        ret=dict()
        if 'id' in request.GET and request.GET['id']:
            assettype = get_object_or_404(AssetType, pk=request.GET.get('id'))
            ret['assettype'] = assettype
        return render(request, 'adm/bsm/assettype_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            assettype = get_object_or_404(AssetType, pk=request.POST.get('id'))
        else:
            assettype = AssetType()
        assettype_form = AssetTypeForm(request.POST, instance=assettype)
        if assettype_form.is_valid():
            assettype_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class AssetTypeDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            AssetType.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class CustomerView(LoginRequiredMixin, View):
    """
    客户信息
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/customer.html', ret)


class CustomerListView(LoginRequiredMixin, View):
    """
    获取客户信息列表
    """
    def get(self, request):
        fields = ['id', 'unit', 'address', 'name', 'phone', 'status', 'belongs_to__name', 'add_time', 'desc']
        filters = dict()
        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        ret = dict(data=list(Customer.objects.values(*fields).filter(**filters)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class CustomerDetailView(LoginRequiredMixin, View):
    """
    客户详情页：查看、修改、新建数据
    """
    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            customer = get_object_or_404(Customer, pk=request.GET.get('id'))
            users = User.objects.exclude(Q(id=customer.belongs_to.id) | Q(is_active=False))
            ret['customer'] = customer
        else:
            users = User.objects.exclude(Q(id=request.user.id) | Q(is_active=False))
        ret['users'] = users
        return render(request, 'adm/bsm/customer_detail.html', ret)

    def post(self, request):
        # res = dict(result=False)
        # if 'id' in request.POST and request.POST['id']:
        #     customer = get_object_or_404(Customer, pk=request.POST.get('id'))
        # else:
        #     customer = Customer()
        # customer_form = CustomerForm(request.POST, instance=customer)
        # if customer_form.is_valid():
        #     customer_form.save()
        #     res['result'] = True
        # return HttpResponse(json.dumps(res), content_type='application/json')
        res = {}
        if 'id' in request.POST and request.POST['id']:
            customer = get_object_or_404(Customer, pk=request.POST.get('id'))
            customer_update_form = CustomerUpdateForm(request.POST, instance=customer)
            if customer_update_form.is_valid():
                customer_update_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(customer_update_form.errors)
                customer_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'customer_form_errors': customer_form_errors[0]
                }

        else:
            customer = Customer()
            customer_create_form = CustomerCreateForm(request.POST, instance=customer)
            if customer_create_form.is_valid():
                customer_create_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(customer_create_form.errors)
                customer_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'customer_form_errors': customer_form_errors[0]
                }
        return HttpResponse(json.dumps(res), content_type='application/json')


class CustomerDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Customer.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class EquipmentTypeView(LoginRequiredMixin, View):
    """
    设备类型
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/bsm/equipmenttype.html', ret)


class EquipmentTypeListView(LoginRequiredMixin, View):
    """
    设备类型列表
    """
    def get(self, request):
        fields = ['id', 'name', 'desc']
        ret = dict(data=list(EquipmentType.objects.values(*fields)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class EquipmentTypeDetailView(LoginRequiredMixin, View):
    """
    资产类型：查看、修改、新建数据
    """
    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment_type = get_object_or_404(EquipmentType, pk=request.GET.get('id'))
            ret['equipment_type'] = equipment_type
        return render(request, 'adm/bsm/equipmenttype_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            equipment_type = get_object_or_404(EquipmentType, pk=request.POST.get('id'))
        else:
            equipment_type = EquipmentType()
        equipment_type_form = EquipmentTypeForm(request.POST, instance=equipment_type)
        if equipment_type_form.is_valid():
            equipment_type_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class EquipmentTypeDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            EquipmentType.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')