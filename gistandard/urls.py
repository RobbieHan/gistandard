"""gistandard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from gistandard.settings import MEDIA_ROOT

import xadmin

from users.views_user import LoginView, IndexView, LogoutView
from system.views import SystemView
from adm.views import AdmView
from personal import views as personal_views
from personal import views_work_order as order

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),
    # 用户登录
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    url(r'^system/$', SystemView.as_view(), name="system"),
    url(r'^system/basic/', include('users.urls', namespace='system-basic')),
    url(r'^system/rbac/', include('rbac.urls', namespace='system-rbac')),
    url(r'^system/tools/', include('system.urls', namespace='system-tools')),

    url(r'^adm/$', AdmView.as_view(), name="adm-main"),
    url(r'^adm/bsm/', include('adm.urls', namespace='adm-bsm')),
    url(r'^adm/equipment/', include('adm.urls_equipment', namespace='adm-equipment')),
    url(r'^adm/asset/', include('adm.urls_asset', namespace='adm-asset')),

    url(r'^personal/$', personal_views.PersonalView.as_view(), name="personal"),
    url(r'^personal/userinfo', personal_views.UserInfoView.as_view(), name="personal-user_info"),
    url(r'^personal/uploadimage', personal_views.UploadImageView.as_view(), name="personal-uploadimage"),
    url(r'^personal/passwordchange', personal_views.PasswdChangeView.as_view(), name="personal-passwordchange"),
    url(r'^personal/phonebook', personal_views.PhoneBookView.as_view(), name="personal-phonebook"),
    url(r'^personal/workorder_Icrt/$', order.WorkOrderView.as_view(), name="personal-workorder_Icrt"),
    url(r'^personal/workorder_Icrt/list', order.WorkOrderListView.as_view(), name="personal-workorder-list"),
    url(r'^personal/workorder_Icrt/create', order.WorkOrderCreateView.as_view(), name="personal-workorder-create"),
    url(r'^personal/workorder_Icrt/detail', order.WorkOrderDetailView.as_view(), name="personal-workorder-detail"),
    url(r'^personal/workorder_Icrt/delete', order.WorkOrderDeleteView.as_view(), name="personal-workorder-delete"),
    url(r'^personal/workorder_Icrt/update', order.WorkOrderUpdateView.as_view(), name="personal-workorder-update"),
    url(r'^personal/workorder_app/$', order.WorkOrderView.as_view(), name="personal-workorder_app"),
    url(r'^personal/workorder_app/send', order.WrokOrderSendView.as_view(), name="personal-workorder-send"),
    url(r'^personal/workorder_rec/$', order.WorkOrderView.as_view(), name="personal-workorder_rec"),
    url(r'^personal/workorder_rec/execute', order.WorkOrderExecuteView.as_view(), name="personal-workorder-execute"),
    url(r'^personal/workorder_rec/finish', order.WorkOrderFinishView.as_view(), name="personal-workorder-finish"),
    url(r'^personal/workorder_rec/upload', order.WorkOrderUploadView.as_view(), name="personal-workorder-upload"),
    url(r'^personal/workorder_rec/return', order.WorkOrderReturnView.as_view(), name="personal-workorder-return"),
    url(r'^personal/workorder_Icrt/upload', order.WorkOrderProjectUploadView.as_view(),
        name="personal-workorder-project-upload"),
    url(r'^personal/workorder_all/$', order.WorkOrderView.as_view(), name="personal-workorder_all"),
    url(r'^personal/document/$', order.WorkOrderDocumentView.as_view(), name="personal-document"),
    url(r'^personal/document/list', order.WorkOrderDocumentListView.as_view(), name="personal-document-list"),

]
