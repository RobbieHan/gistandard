import json
import re
from datetime import datetime, timedelta

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Equipment, EquipmentType, Customer, Supplier, ServiceInfo
from .forms import EquipmentCreateForm, EquipmentUpdateForm

User = get_user_model()


class EquipmentView(LoginRequiredMixin, View):
    """
    设备管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        equipment_types = EquipmentType.objects.all()
        filters = dict()
        if request.user.department_id == 9:  # 销售部门只能看自己的设备信息
            filters['belongs_to_id'] = request.user.id
        customers = Customer.objects.filter(**filters).order_by('unit')
        ret['equipment_types'] = equipment_types
        ret['customers'] = customers

        return render(request, 'adm/equipment/equipment.html', ret)


class EquipmentListView(LoginRequiredMixin, View):
    """
    设备管理：设备列表
    """

    def get(self, request):
        fields = ['id', 'number', 'equipment_type__name', 'equipment_model', 'buy_date', 'warranty_date',
                  'customer__unit', 'customer__belongs_to__name']
        filters = dict()
        if request.user.department_id == 9:  # 销售部门只能看自己的设备信息
            filters['customer__belongs_to_id'] = request.user.id
        if 'select' in request.GET and request.GET['select']:
            select = int(request.GET['select'])
            if select == 0:
                date_time = datetime.today()
                filters['warranty_date__lte'] = date_time
            if select == 1:
                now = datetime.today()
                date_time = now + timedelta(days=365)
                filters['warranty_date__range'] = (now, date_time)

        if 'number' in request.GET and request.GET['number']:
            filters['number__icontains'] = request.GET['number']
        if 'equipment_type' in request.GET and request.GET['equipment_type']:
            filters['equipment_type'] = request.GET['equipment_type']
        if 'equipment_model' in request.GET and request.GET['equipment_model']:
            filters['equipment_model__icontains'] = request.GET['equipment_model']
        if 'customer' in request.GET and request.GET['customer']:
            filters['customer'] = request.GET['customer']
        ret = dict(data=list(Equipment.objects.filter(**filters).values(*fields).order_by('-id')))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class EquipmentCreateView(LoginRequiredMixin, View):
    """
    设备管理：新建和修改资产数据
    """

    def get(self, request):
        ret = dict()
        filters = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
            ret['equipment'] = equipment
        equipment_type = EquipmentType.objects.values()

        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        suppliers = Supplier.objects.values().filter(**filters)
        ret['equipment_type'] = equipment_type
        ret['customer'] = customer
        ret['suppliers'] = suppliers

        # 获取登陆用户的角色组返回给前端，用来控制费用核算的显示状态
        user_info = User.objects.get(id=request.user.id)
        roles = user_info.roles.values()
        role_list = [role['title'] for role in roles if role['title'] == '核算']
        if role_list:
            ret['role_list'] = role_list[0]
        return render(request, 'adm/equipment/equipment_create.html', ret)

    def post(self, request):
        res = {}
        # if 'id' in request.POST and request.POST['id']:
        #     equipment = get_object_or_404(Equipment, pk=request.POST.get('id'))
        # else:
        #     equipment = Equipment()
        # equipment_form = EquipmentForm(request.POST, instance=equipment)
        # if equipment_form.is_valid():
        #     equipment_form.save()
        # else:
        #     pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
        #     errors = str(equipment_form.errors)
        #     equipment_form_errors = re.findall(pattern, errors)
        #     res = {
        #         'status': 'fail',
        #         'equipment_form_errors': equipment_form_errors[0]
        #     }

        #  分别多修建和更新两种行为的forms验证，避免添加重复的NT设备
        if 'id' in request.POST and request.POST['id']:
            equipment = get_object_or_404(Equipment, pk=request.POST.get('id'))
            equipment_update_form = EquipmentUpdateForm(request.POST, instance=equipment)
            if equipment_update_form.is_valid():
                equipment_update_form.save()
                # new_equipment = equipment_update_form.save(commit=False)
                # new_equipment.save()
                # equipment_update_form.save_m2m()

                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(equipment_update_form.errors)
                equipment_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'equipment_form_errors': equipment_form_errors[0]
                }
        else:
            equipment = Equipment()
            equipment_create_form = EquipmentCreateForm(request.POST, instance=equipment)
            if equipment_create_form.is_valid():
                equipment_create_form.save()
                res['status'] = 'success'
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(equipment_create_form.errors)
                equipment_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                  'equipment_form_errors': equipment_form_errors[0]
                }
        return HttpResponse(json.dumps(res), content_type='application/json')


class EquipmentDetailView(LoginRequiredMixin, View):
    """
    设备管理：详情页面
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment = get_object_or_404(Equipment, pk=request.GET.get('id'))
            ret['equipment'] = equipment
        service_info_all = equipment.service_info.all()
        dates = service_info_all.datetimes('add_time', 'day')
        services = []
        for date in dates:
            start = date
            end = date + timedelta(days=1)
            service_info = service_info_all.filter(add_time__range=(start, end))
            service_info_dict = {
                "date": date,
                "content": service_info
            }

            services.append(service_info_dict)
        ret['services'] = services
        return render(request, 'adm/equipment/equipment_detail.html', ret)


class EquipmentDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Equipment.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class ServiceInfoUpdateView(LoginRequiredMixin, View):
    """
    设备维保更新记录
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            equipment_id = request.GET['id']
            ret['equipment_id'] = equipment_id
        return render(request, 'adm/equipment/service_info_update.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            equipment = get_object_or_404(Equipment, pk=request.POST.get('id'))
            if 'content' in request.POST and request.POST['content']:
                content = request.POST['content']
                writer_id = request.user.id
                service_info = ServiceInfo(content=content, writer_id=writer_id)
                service_info.save()
                equipment.service_info.add(service_info)
                res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')
