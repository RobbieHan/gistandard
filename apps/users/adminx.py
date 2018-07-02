# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/10/21

import xadmin

from .models import Structure


class StructureAdmin(object):
    list_display = ['title', 'type', 'parent']
    list_filter = ['title', 'type', 'parent']

xadmin.site.register(Structure, StructureAdmin)

