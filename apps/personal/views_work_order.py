import json
import re

from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from .models import WorkOrder, WorkOrderRecord
from .forms import WorkOrderCreateForm, WorkOrderUpdateForm, WorkOrderRecordForm, WorkOrderRecordUploadForm, WorkOrderProjectUploadForm
from adm.models import Customer
from rbac.models import Role

from utils.toolkit import ToolKit, SendMessage
User = get_user_model()


class WorkOrderView(LoginRequiredMixin, View):
    """
    工单视图：根据前端请求的URL 分为个视图：我创建的工单、我审批的工单和我收到的工单
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        status_list = []
        filters = dict()
        for work_order_status in WorkOrder.status_choices:
            status_dict = dict(item=work_order_status[0], value=work_order_status[1])
            status_list.append(status_dict)
        if request.user.department_id == 9:  # 销售部门只能看自己的设备信息
            filters['belongs_to_id'] = request.user.id
        customers = Customer.objects.filter(**filters).order_by('unit')
        ret['status_list'] = status_list
        ret['customers'] = customers
        return render(request, 'personal/workorder/workorder.html', ret)


class WorkOrderListView(LoginRequiredMixin, View):
    """
    工单列表：通过前端传递回来的url来区分不同视图，返回相应列表数据
    """
    def get(self, request):
        fields = ['id', 'number', 'title', 'type', 'status', 'do_time', 'customer__unit', 'proposer__name']
        filters = dict()
        if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_Icrt/':
            filters['proposer_id'] = request.user.id
        if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_app/':
            filters['approver_id'] = request.user.id
            filters['status__in'] = ['0', '2', '3', '4', '5']  # 审批人视图可以看到的工单状态
        if 'main_url' in request.GET and request.GET['main_url'] == '/personal/workorder_rec/':
            filters['receiver_id'] = request.user.id
        if 'number' in request.GET and request.GET['number']:
            filters['number__icontains'] = request.GET['number']
        if 'workorder_status' in request.GET and request.GET['workorder_status']:
            filters['status'] = request.GET['workorder_status']
        if 'customer' in request.GET and request.GET['customer']:
            filters['customer_id'] = request.GET['customer']
        ret = dict(data=list(WorkOrder.objects.filter(**filters).values(*fields).order_by('-add_time')))

        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderCreateView(LoginRequiredMixin, View):

    def get(self, request):
        type_list = []
        filters = dict()
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:  # 新建工单时销售部门只能选择自己的用户信息
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        try:
            number = WorkOrder.objects.latest('number').number
        except WorkOrder.DoesNotExist:
            number = ""
        new_number = ToolKit.bulidNumber('SX', 9, number)
        ret = {
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
            'new_number': new_number
        }
        return render(request, 'personal/workorder/workorder_create.html', ret)

    def post(self, request):
        res = dict()
        work_order = WorkOrder()
        work_order_form = WorkOrderCreateForm(request.POST, instance=work_order)
        if work_order_form.is_valid():
            work_order_form.save()
            res['status'] = 'success'
            if work_order.status == "2":
                res['status'] = 'submit'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'submit_send'
                except Exception:
                    pass
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(work_order_form.errors)
            work_order_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'work_order_form_errors': work_order_form_errors[0]
            }
        return HttpResponse(json.dumps(res), content_type='application/json')


class WorkOrderDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        admin_user_list = []
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
            work_order_record = work_order.workorderrecord_set.all().order_by('add_time')
            try:
                role = Role.objects.get(title="管理")
                admin_user_ids = role.userprofile_set.values('id')
                for admin_user_id in admin_user_ids:
                    admin_user_list.append(admin_user_id['id'])
            except Exception:
                pass
            user_list = [work_order.proposer_id, work_order.approver_id, work_order.receiver_id]
            user_list.extend(admin_user_list)

            # 和工单无关联的用户禁止通过手动指定ID的形式非法获取数据
            if request.user.id in user_list:
                ret['work_order'] = work_order
                ret['work_order_record'] = work_order_record
            else:
                ret['ban'] = 'ban'
        return render(request, 'personal/workorder/workorder_detail.html', ret)


class WorkOrderDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            status = get_object_or_404(WorkOrder, pk=request.POST['id']).status
            if int(status) <= 1:
                id_list = map(int, request.POST.get('id').split(','))
                WorkOrder.objects.filter(id__in=id_list).delete()
                ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class WorkOrderUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        type_list = []
        filters = dict()
        if 'id' in request.GET and request.GET['id']:
            work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        for work_order_type in WorkOrder.type_choices:
            type_dict = dict(item=work_order_type[0], value=work_order_type[1])
            type_list.append(type_dict)
        if request.user.department_id == 9:
            filters['belongs_to_id'] = request.user.id
        customer = Customer.objects.values().filter(**filters)
        role = get_object_or_404(Role, title='审批')
        approver = role.userprofile_set.all()
        ret = {
            'work_order': work_order,
            'type_list': type_list,
            'customer': customer,
            'approver': approver,
        }
        return render(request, 'personal/workorder/workorder_update.html', ret)

    def post(self, request):
        res = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.POST['id'])
        work_order_form = WorkOrderUpdateForm(request.POST, instance=work_order)
        if int(work_order.status) <= 1:
            if work_order_form.is_valid():
                work_order_form.save()
                res['status'] = 'success'
                if work_order.status == "2":
                    res['status'] = 'submit'
                    try:
                        SendMessage.send_workorder_email(request.POST['number'])
                        res['status'] = 'submit_send'
                    except Exception:
                        pass
            else:
                pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
                errors = str(work_order_form.errors)
                work_order_form_errors = re.findall(pattern, errors)
                res = {
                    'status': 'fail',
                    'work_order_form_errors': work_order_form_errors[0]
                }
        else:
            res['status'] = 'ban'
        return HttpResponse(json.dumps(res), content_type='application/json')


class WrokOrderSendView(LoginRequiredMixin, View):
    """
    工单派发： 由审批人完成工单派发，记录派发状态 '1'，
    """

    def get(self, request):
        ret = dict()
        engineers = User.objects.filter(department__title='技术部')
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['engineers'] = engineers
        ret['work_order'] = work_order
        ret['record_type'] = "1"
        return render(request, 'personal/workorder/workorder_send.html', ret)

    def post(self, request):
        res = dict(status='fail')
        work_order_record_form = WorkOrderRecordForm(request.POST)
        if work_order_record_form.is_valid():
            work_order = get_object_or_404(WorkOrder, pk=request.POST['work_order'])
            status = work_order.status
            if status in ['0', '2'] and request.user.id == work_order.approver_id:
                work_order_record_form.save()
                work_order.receiver_id = request.POST['receiver']
                work_order.status = "3"
                work_order.do_time = request.POST['do_time']
                work_order.save()
                res['status'] = 'success'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'success_send'
                except Exception:
                    pass

            else:
                res['status'] = 'ban'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')



class WorkOrderExecuteView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['work_order'] = work_order
        ret['record_type'] = "2"
        return render(request, 'personal/workorder/workorder_execute.html', ret)

    def post(self, request):
        res = dict(status='fail')
        work_order_record_form = WorkOrderRecordForm(request.POST)
        work_order = get_object_or_404(WorkOrder, pk=request.POST['work_order'])
        if work_order_record_form.is_valid() and work_order.receiver_id == request.user.id:
            status = work_order.status
            if status == '3' and request.user.id == work_order.receiver_id:
                work_order_record_form.save()
                work_order.status = "4"
                work_order.save()
                res['status'] = 'success'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'success_send'
                except Exception as e:
                    pass
            else:
                res['status'] = 'ban'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderFinishView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['work_order'] = work_order
        ret['record_type'] = "3"
        return render(request, 'personal/workorder/workorder_finish.html', ret)

    def post(self, request):
        res = dict(status='fail')
        work_order_record_form = WorkOrderRecordForm(request.POST)
        work_order = get_object_or_404(WorkOrder, pk=request.POST['work_order'])
        if work_order_record_form.is_valid() and work_order.proposer.id == request.user.id:
            status = work_order.status
            if status == '4' and request.user.id == work_order.proposer_id:
                work_order_record_form.save()
                work_order.status = "5"
                work_order.save()
                res['status'] = 'success'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'success_send'
                except Exception as e:
                    pass
            else:
                res['status'] = 'ban'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderReturnView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['work_order'] = work_order
        ret['record_type'] = "0"
        return render(request, 'personal/workorder/workorder_return.html', ret)

    def post(self, request):
        res = dict(status='fail')
        work_order_record_form = WorkOrderRecordForm(request.POST)
        work_order = get_object_or_404(WorkOrder, pk=request.POST['work_order'])
        if work_order_record_form.is_valid():
            status = work_order.status
            if status == '3':
                work_order_record_form.save()
                work_order.status = "0"
                work_order.save()
                res['status'] = 'success'
                try:
                    SendMessage.send_workorder_email(request.POST['number'])
                    res['status'] = 'success_send'
                except Exception as e:
                    pass
                work_order.receiver = None
                work_order.save()
            else:
                res['status'] = 'ban'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')

class WorkOrderUploadView(LoginRequiredMixin, View):
    """
    上传配置资料：工单执行记录配置资料上传
    """
    def get(self, request):
        ret = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['work_order'] = work_order
        return render(request, 'personal/workorder/workorder_upload.html', ret)

    def post(self, request):
        res = dict(status='fail')
        #work_order_record = get_object_or_404(WorkOrderRecord, name_id=request.user.id, work_order_id=request.POST['id'])
        filters = dict(name_id=request.user.id, work_order_id=request.POST['id'])
        work_order_record = WorkOrderRecord.objects.filter(**filters).last()
        work_order_record_upload_form = WorkOrderRecordUploadForm(request.POST, request.FILES, instance=work_order_record)
        if work_order_record_upload_form.is_valid():
            work_order_record_upload_form.save()
            res['status'] = 'success'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderProjectUploadView(LoginRequiredMixin, View):
    """
    上传项目资料：工单内容项目资料上传
    """
    def get(self, request):
        ret = dict()
        work_order = get_object_or_404(WorkOrder, pk=request.GET['id'])
        ret['work_order'] = work_order
        return render(request, 'personal/workorder/workorder_project_upload.html', ret)

    def post(self, request):
        res = dict(status='fail')
        work_order = get_object_or_404(WorkOrder, pk=request.POST['id'])
        work_order_project_upload_form = WorkOrderProjectUploadForm(request.POST, request.FILES, instance=work_order)
        if work_order_project_upload_form.is_valid() and request.user.id == work_order.proposer_id:
            work_order_project_upload_form.save()
            res['status'] = 'success'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')


class WorkOrderDocumentView(LoginRequiredMixin, View):
    """
    工单文档
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)

        return render(request, 'personal/workorder/document.html', ret)


class WorkOrderDocumentListView(LoginRequiredMixin, View):
    """
    工单文档列表
    """
    def get(self, request):
        fields = ['work_order__number', 'work_order__customer__unit', 'name__name', 'add_time', 'file_content']
        ret = dict(data=list(WorkOrderRecord.objects.filter(~Q(file_content='')).values(*fields).order_by('-add_time')))

        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')
