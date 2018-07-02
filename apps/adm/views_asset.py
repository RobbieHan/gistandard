import json
import re

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup
from .models import Asset, AssetType, AssetLog, AssetFile
from .forms import AssetCreateForm, AssetUpdateForm, AssetUploadForm
from rbac.models import Role


User = get_user_model()


class AssetView(LoginRequiredMixin, View):
    """
    资产管理
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        status_list = []
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_types = AssetType.objects.all()
        ret['status_list'] = status_list
        ret['asset_types'] = asset_types
        return render(request, 'adm/asset/asset.html', ret)


class AssetListView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'assetNum', 'assetType__name', 'brand', 'model', 'warehouse', 'status', 'owner__name', 'operator', 'add_time']
        filters = dict()

        if 'assetNum' in request.GET and request.GET['assetNum']:
            filters['assetNum__icontains'] = request.GET['assetNum']
        if 'assetType' in request.GET and request.GET['assetType']:
            filters['assetType'] = request.GET['assetType']
        if 'model' in request.GET and request.GET['model']:
            filters['model__icontains'] = request.GET['model']
        if 'status' in request.GET and request.GET['status']:
            filters['status'] = request.GET['status']
        ret = dict(data=list(Asset.objects.filter(**filters).values(*fields)))
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class AssetCreateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        status_list = []
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_type = AssetType.objects.values()
        role = get_object_or_404(Role, title="销售")
        user_info = role.userprofile_set.all()
        ret['asset_type'] = asset_type
        ret['user_info'] = user_info
        ret['status_list'] = status_list
        return render(request, 'adm/asset/asset_create.html', ret)

    def post(self, request):
        res = dict()
        asset_create_form = AssetCreateForm(request.POST)
        if asset_create_form.is_valid():
            asset_create_form.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(asset_create_form.errors)
            asset_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'asset_form_errors': asset_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')


class AssetUpdateView(LoginRequiredMixin, View):

    def get(self, request):
        ret = dict()
        status_list = []
        if 'id' in request.GET and request.GET['id']:
            asset = get_object_or_404(Asset, pk=request.GET['id'])
            ret['asset'] = asset
        for status in Asset.asset_status:
            status_dict = dict(item=status[0], value=status[1])
            status_list.append(status_dict)
        asset_type = AssetType.objects.values()
        role = get_object_or_404(Role, title="销售")
        user_info = role.userprofile_set.all()
        ret['asset_type'] = asset_type
        ret['user_info'] = user_info
        ret['status_list'] = status_list
        return render(request, 'adm/asset/asset_update.html', ret)

    def post(self, request):
        res = dict()
        asset = get_object_or_404(Asset, pk=request.POST['id'])
        asset_update_form = AssetUpdateForm(request.POST, instance=asset)
        if asset_update_form.is_valid():
            asset_update_form.save()
            status = asset.get_status_display()
            asset_log = AssetLog()
            asset_log.asset_id = asset.id
            asset_log.operator = request.user.name
            asset_log.desc = """
            用户信息：{}  || 责任人：{}  || 资产状态：{}""".format(
                asset_update_form.cleaned_data.get("customer"),
                asset_update_form.cleaned_data.get("owner"),
                status,
            )
            asset_log.save()
            res['status'] = 'success'
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(asset_update_form.errors)
            asset_form_errors = re.findall(pattern, errors)
            res = {
                'status': 'fail',
                'asset_form_errors': asset_form_errors[0]
            }

        return HttpResponse(json.dumps(res), content_type='application/json')

class AssetDetailView(LoginRequiredMixin, View):
    """
    资产管理：详情页面
    """
    def get(self, request):
        ret = dict()
        if 'id' in request.GET and request.GET['id']:
            asset = get_object_or_404(Asset, pk=request.GET.get('id'))
            asset_log = asset.assetlog_set.all()
            asset_file = asset.assetfile_set.all()
            ret['asset'] = asset
            ret['asset_log'] = asset_log
            ret['asset_file'] = asset_file
        return render(request, 'adm/asset/asset_detail.html', ret)


class AssetDeleteView(LoginRequiredMixin, View):

    def post(self, request):
        ret = dict(result=False)
        if 'id' in request.POST and request.POST['id']:
            id_list = map(int, request.POST.get('id').split(','))
            Asset.objects.filter(id__in=id_list).delete()
            ret['result'] = True
        return HttpResponse(json.dumps(ret), content_type='application/json')


class AssetUploadView(LoginRequiredMixin, View):
    """
    上传配置资料：工单执行记录配置资料上传
    """
    def get(self, request):
        ret = dict()
        asset = get_object_or_404(Asset, pk=request.GET['id'])
        ret['asset'] = asset
        return render(request, 'adm/asset/asset_upload.html', ret)

    def post(self, request):
        res = dict(status='fail')
        asset_file = AssetFile()
        asset_upload_form = AssetUploadForm(request.POST, request.FILES, instance=asset_file)
        if asset_upload_form.is_valid():
            asset_upload_form.save()
            res['status'] = 'success'
        return HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json')