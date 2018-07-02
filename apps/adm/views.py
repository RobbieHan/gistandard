from django.shortcuts import render
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin
from rbac.models import Menu
from system.models import SystemSetup

class AdmView(LoginRequiredMixin, View):
    """
    行政
    """
    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'adm/adm_index.html', ret)