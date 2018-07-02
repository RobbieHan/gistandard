import json

from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import get_object_or_404

User = get_user_model()

from django.views.generic.base import View
from django.http import HttpResponse

from utils.mixin_utils import LoginRequiredMixin
from .models import Menu
from .forms import MenuForm
from system.models import SystemSetup



class MenuView(LoginRequiredMixin, View):
    """
    菜单管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/rbac/menu-list.html', ret)


class MenuListView(LoginRequiredMixin, View):
    """
    获取菜单列表
    """

    def get(self, request):
        fields = ['id', 'title', 'code', 'url', 'is_top', 'parent__title']
        ret = dict(data=list(Menu.objects.values(*fields).order_by('id')))
        return HttpResponse(json.dumps(ret), content_type='application/json')


class MenuListDetailView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            menu = get_object_or_404(Menu, pk=request.GET.get('id'))
            ret['menu'] = menu
        menu_list = Menu.objects.exclude(id=request.GET.get('id'))
        ret['menu_list'] = menu_list
        return render(request, 'system/rbac/menu_detail.html', ret)

    def post(self, request):
        res = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            menu = get_object_or_404(Menu, pk=request.POST.get('id'))
        else:
            menu = Menu()
        menu_form = MenuForm(request.POST, instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            res['result'] = True
        return HttpResponse(json.dumps(res), content_type='application/json')

