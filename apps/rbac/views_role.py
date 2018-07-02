import json

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponse

from utils.mixin_utils import LoginRequiredMixin
from .models import Role, Menu
from system.models import SystemSetup

class RoleView(LoginRequiredMixin, View):
    """
    角色管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/rbac/role-list.html', ret)


class RoleListView(LoginRequiredMixin, View):
    """
    获取角色数据列表
    """

    def get(self, request):
        fields = ['id', 'title']
        ret = dict(data=list(Role.objects.values(*fields).exclude(id=1)))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class RoleDetailView(LoginRequiredMixin, View):
    """
    组织架构详情页：查看、修改、新建数据
    """

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            ret = dict(role=get_object_or_404(Role, pk=request.GET.get('id')))

        return render(request, 'system/rbac/role_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            role = get_object_or_404(Role, pk=request.POST.get('id'))
        else:
            role = Role()
        if request.POST.get('title'):
            role.title = request.POST.get('title')
            role.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class RoleDeleteView(LoginRequiredMixin, View):
    """
    删除数据：支持删除单条记录和批量删除
    """

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Role.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class Role2MenuView(LoginRequiredMixin, View):
    """
    角色绑定菜单
    """
    def get(self, request):
        if 'id' in request.GET and request.GET['id']:
            role = get_object_or_404(Role, pk=request.GET.get('id'))
            ret = dict(role=role)
            return render(request, 'system/rbac/role_menu.html', ret)

    def post(self, request):
        res = dict(result=False)
        role = get_object_or_404(Role, pk=request.POST.get('id'))
        tree = json.loads(self.request.POST['tree'])
        role.permissions.clear()
        for menu in tree:
            if menu['checked'] is True:
                menu_checked = get_object_or_404(Menu, pk=menu['id'])
                role.permissions.add(menu_checked)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')


class Role2MenuListView(LoginRequiredMixin, View):
    """
    获取zTree菜单列表
    """
    def get(self, request):
        fields = ['id', 'title', 'parent']
        if 'id' in request.GET and request.GET['id']:
            role = Role.objects.get(id=request.GET.get('id'))
            role_menus = role.permissions.values(*fields)
            ret = dict(data=list(role_menus))
        else:
            menus = Menu.objects.all()
            ret = dict(data=list(menus.values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class Role2UserView(LoginRequiredMixin, View):
    """
    角色关联用户
    """

    def get(self, request):
        if 'id' in request.GET and request.GET['id']:
            role = get_object_or_404(Role, pk=int(request.GET.get('id')))
            added_users = role.userprofile_set.all()
            all_users = User.objects.exclude(username='admin')
            un_add_users = set(all_users).difference(added_users)
            ret = dict(role=role, added_users=added_users, un_add_users=list(un_add_users))
        return render(request, 'system/rbac/role_user.html', ret)

    def post(self, request):
        res = dict(result=False)
        id_list = None
        role = get_object_or_404(Role, pk=int(request.POST.get('id')))
        if 'to' in request.POST and request.POST['to']:
            id_list = map(int, request.POST.getlist('to', []))
        role.userprofile_set.clear()
        if id_list:
            for user in User.objects.filter(id__in=id_list):
                role.userprofile_set.add(user)
        res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')