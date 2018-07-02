import json
import re
import calendar
from datetime import date, timedelta

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .forms import ImageUploadForm, UserUpdateForm
from users.forms import AdminPasswdChangeForm
from .models import WorkOrder
from rbac.models import Role

from utils.toolkit import get_month_work_order_count, get_year_work_order_count

User = get_user_model()


class PersonalView(LoginRequiredMixin, View):
    """
    我的工作台
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        # (('0', '工单已退回'), ('1', '新建-保存'), ('2', '提交-等待审批'), ('3', '已审批-等待执行'), ('4', '已执行-等待确认'), ('5', '工单已完成'))
        # 当月个人工单状态统计
        work_order = WorkOrder.objects.filter(Q(add_time__range=(start_date, end_date)),
                                              Q(proposer_id=request.user.id) |
                                              Q(receiver_id=request.user.id) |
                                              Q(approver_id=request.user.id)
                                              )
        ret['work_order_1'] = work_order.filter(status="1").count()
        ret['work_order_2'] = work_order.filter(status="2").count()
        ret['work_order_3'] = work_order.filter(status="3").count()
        ret['work_order_4'] = work_order.filter(status="4").count()
        ret['start_date'] = start_date

        role = Role.objects.get(title='销售')
        if 'value' in request.GET and int(request.GET['value']) == 1:
            role = Role.objects.get(title='技术')
        if role:
            users = role.userprofile_set.filter(is_active=1).values('id', 'name')
            month_work_order_count = get_month_work_order_count(users, value=int(request.GET.get('value', 0)))
            year_work_order_count = get_year_work_order_count(users, value=int(request.GET.get('value', 0)))
            ret['month_work_order_count'] = month_work_order_count
            ret['year_work_order_count'] = year_work_order_count

        return render(request, 'personal/personal_index.html', ret)


class UserInfoView(LoginRequiredMixin, View):
    """
    个人中心：个人信息查看修改和修改
    """

    def get(self, request):
        return render(request, 'personal/userinfo/user_info.html')

    def post(self, request):
        ret = dict(status="fail")
        user = User.objects.get(id=request.POST['id'])
        user_update_form = UserUpdateForm(request.POST, instance=user)
        if user_update_form.is_valid():
            user_update_form.save()
            ret = {"status": "success"}
        return HttpResponse(json.dumps(ret), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    """
    个人中心：上传头像
        """

    def post(self, request):
        ret = dict(result=False)
        image_form = ImageUploadForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class PasswdChangeView(LoginRequiredMixin, View):
    """
    登陆用户修改个人密码
    """

    def get(self, request):
        ret = dict()
        user = get_object_or_404(User, pk=int(request.user.id))
        ret['user'] = user
        return render(request, 'personal/userinfo/passwd-change.html', ret)

    def post(self, request):

        user = get_object_or_404(User, pk=int(request.user.id))
        form = AdminPasswdChangeForm(request.POST)
        if form.is_valid():
            new_password = request.POST.get('password')
            user.set_password(new_password)
            user.save()
            ret = {'status': 'success'}
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(form.errors)
            admin_passwd_change_form_errors = re.findall(pattern, errors)
            ret = {
                'status': 'fail',
                'admin_passwd_change_form_errors': admin_passwd_change_form_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class PhoneBookView(LoginRequiredMixin, View):
    def get(self, request):
        fields = ['name', 'mobile', 'email', 'post', 'department__title', 'image']
        ret = dict(linkmans=list(User.objects.exclude(username='admin').filter(is_active=1).values(*fields)))
        return render(request, 'personal/phonebook/phonebook.html', ret)
