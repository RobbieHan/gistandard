import json
import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, UserUpdataForm, UserCreateForm, AdminPasswdChangeForm
from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Role
from apps.users.models import Structure
from system.models import SystemSetup


class UserBackend(ModelBackend):
    """
    自定义用户验证: setting中对应配置
    AUTHENTICATION_BACKENDS = (
        'users.views.UserBackend',
        )
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        # if request.user.is_authenticated():
        #     return render(request, 'index.html')
        # else:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return HttpResponseRedirect('/personal/')

class LoginView(View):
    '''
    用户登录认证，通过form表单进行输入合规验证
    '''

    def get(self, request):
        if not request.user.is_authenticated():
            ret = (SystemSetup.getSystemSetupLastData())
            return render(request, 'system/users/login.html', ret)
        else:
            return HttpResponseRedirect('/personal/')

    def post(self, request):
        redirect_to = request.GET.get('next', '/personal/')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    msg = "用户未激活！"
                    ret = {"msg": msg, "login_form": login_form}
                    return render(request, "system/users/login.html", ret)
            else:
                msg = "用户名或密码错误！"
                ret = {"msg": msg, "login_form": login_form}
                return render(request, "system/users/login.html", ret)

        else:
            msg = "用户名和密码不能够为空！"
            ret = {"msg": msg, "login_form": login_form}
            return render(request, "system/users/login.html", ret)


class LogoutView(View):
    '''
    用户登出
    '''

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class UserView(LoginRequiredMixin, View):
    """
    用户管理
    """

    def get(self, request):
        ret = SystemSetup.getSystemSetupLastData()
        return render(request, 'system/users/user-list.html', ret)


class UserListView(LoginRequiredMixin, View):
    """
    获取用户列表信息
    """

    def get(self, request):
        fields = ['id', 'name', 'gender', 'mobile', 'email', 'department__title', 'post', 'superior__name', 'is_active']
        filters = dict()
        if 'select' in request.GET and request.GET.get('select'):
            filters['is_active'] = request.GET.get('select')
        ret = dict(data=list(User.objects.filter(**filters).values(*fields).exclude(username='admin')))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class UserDetailView(LoginRequiredMixin, View):
    """
    用户详情页面:用户查看修改用户详情信息（管理员修改用户信息和用户修改个人信息）
    """

    def get(self, request):
        user = get_object_or_404(User, pk=int(request.GET['id']))
        users = User.objects.exclude(Q(id=int(request.GET['id'])) | Q(username='admin'))
        structures = Structure.objects.values()
        roles = Role.objects.exclude(id=1)
        user_roles = user.roles.all()

        ret = {
            'user': user,
            'structures': structures,
            'users': users,
            'roles': roles,
            'user_roles': user_roles,

        }

        return render(request, 'system/users/user_detail.html', ret)


class UserUpdataView(LoginRequiredMixin, View):
    """
    提交修改,保存数据
    """

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            user = get_object_or_404(User, pk=int(request.POST['id']))
        else:
            user = get_object_or_404(User, pk=int(request.user.id))
        user_updata_form = UserUpdataForm(request.POST, instance=user)
        if user_updata_form.is_valid():
            user_updata_form.save()
            ret = {"status": "success"}
        else:
            ret = {'status': 'fail', 'message': user_updata_form.errors}
        return HttpResponse(json.dumps(ret), content_type='application/json')


class UserCreateView(LoginRequiredMixin, View):
    """
    添加用户
    """

    def get(self, request):
        users = User.objects.exclude(username='admin')
        structures = Structure.objects.values()
        roles = Role.objects.exclude(id=1)

        ret = {
            'users': users,
            'structures': structures,
            'roles': roles,
        }
        return render(request, 'system/users/user_create.html', ret)

    def post(self, request):
        user_create_form = UserCreateForm(request.POST)
        if user_create_form.is_valid():
            new_user = user_create_form.save(commit=False)
            new_user.password = make_password(user_create_form.cleaned_data['password'])
            new_user.save()
            user_create_form.save_m2m()
            ret = {'status': 'success'}
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(user_create_form.errors)
            user_create_form_errors = re.findall(pattern, errors)
            ret = {
                'status': 'fail',
                'user_create_form_errors': user_create_form_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class UserDeleteView(LoginRequiredMixin, View):
    """
    删除数据：支持删除单条记录和批量删除
    """

    def post(self, request):
        id_nums = request.POST.get('id')
        User.objects.extra(where=["id IN (" + id_nums + ")"]).delete()
        ret = {
            'result': 'true',
            'message': '数据删除成功！'
        }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class UserEnableView(LoginRequiredMixin, View):
    """
    启用用户：单个或批量启用
    """

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            id_nums = request.POST.get('id')
            queryset = User.objects.extra(where=["id IN(" + id_nums + ")"])
            queryset.filter(is_active=False).update(is_active=True)
            ret = {'result': 'True'}
        return HttpResponse(json.dumps(ret), content_type='application/json')


class UserDisableView(LoginRequiredMixin, View):
    """
    启用用户：单个或批量启用
    """

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            id_nums = request.POST.get('id')
            queryset = User.objects.extra(where=["id IN(" + id_nums + ")"])
            queryset.filter(is_active=True).update(is_active=False)
            ret = {'result': 'True'}
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AdminPasswdChangeView(LoginRequiredMixin, View):
    """
    管理员修改用户列表中的用户密码
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            user = get_object_or_404(User, pk=int(request.GET.get('id')))
            ret['user'] = user
        return render(request, 'system/users/adminpasswd-change.html', ret)

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            user = get_object_or_404(User, pk=int(request.POST.get('id')))
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
