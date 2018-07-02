# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/10/12

import re

from django import forms
from .models import SystemSetup


class SystemSetupForm(forms.ModelForm):
    class Meta:
        model = SystemSetup
        fields = '__all__'