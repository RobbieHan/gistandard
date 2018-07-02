# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/12/20

from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

