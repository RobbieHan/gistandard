# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/19

import xadmin

from .models import SystemSetup, EmailSetup


class SystemSetupAdmin(object):
    list_display = ['loginTitle', 'mainTitle', 'headTitle', 'copyright', 'url']
    list_filter = ['loginTitle', 'mainTitle', 'headTitle', 'url']


class EmailSetupAdmin(object):
    list_display = ['emailHost', 'emailPort', 'emailUser', 'emailPassword']


xadmin.site.register(SystemSetup, SystemSetupAdmin)
xadmin.site.register(EmailSetup, EmailSetupAdmin)
