# -*- coding: UTF-8 -*-
# __author__ : RobbieHan
# __data__  : 2017/10/12

import re

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

from apps.users.models import Structure


class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={"required": "请填写用户名"})
    password = forms.CharField(required=True, error_messages={"required": u"请填写密码"})


class UserUpdataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'gender', 'birthday', 'username', 'mobile', 'email', 'joined_date', 'department', 'post',
                  'superior', 'is_active', 'roles']


class UserCreateForm(forms.ModelForm):
    """
    创建用户表单，进行字段验证
    """

    password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"密码不能为空",
            "min_length": "密码长度最少6位数",
        })

    confirm_password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"确认密码不能为空",
            "min_length": "密码长度最少6位数",
        })

    class Meta:
        model = User
        fields = ['name', 'gender', 'birthday', 'username', 'mobile',
                  'email', 'joined_date', 'department', 'post',
                  'superior', 'is_active', 'roles', 'password']

        error_messages = {
            "name": {"required": "姓名不能为空"},
            "username": {"required": "用户名不能为空"},
            "email": {"required": "邮箱不能为空"},
            "mobile": {
                    "required": "手机号码不能为空",
                    "max_length": "输入有效的手机号码",
                    "min_length": "输入有效的手机号码"
            }

        }

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        username = cleaned_data.get("username")
        mobile = cleaned_data.get("mobile", "")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if User.objects.filter(username=username).count():
            raise forms.ValidationError('用户名：{}已存在'.format(username))

        if password != confirm_password:
            raise forms.ValidationError("两次密码输入不一致")

        if User.objects.filter(mobile=mobile).count():
            raise forms.ValidationError('手机号码：{}已存在'.format(mobile))

        # 手机号码合法性验证
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, mobile):
            raise forms.ValidationError("手机号码非法")

        if User.objects.filter(email=email).count():
            raise forms.ValidationError('邮箱：{}已存在'.format(email))


class AdminPasswdChangeForm(forms.Form):
    """
    管理员用户修改用户列表中的用户密码
    """
    # def __init__(self, *args, **kwargs):
    #     super(AdminPasswdChangeForm, self).__init__(*args, **kwargs)

    password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"密码不能为空"
        })

    confirm_password = forms.CharField(
        required=True,
        min_length=6,
        max_length=20,
        error_messages={
            "required": u"确认密码不能为空"
        })

    def clean(self):
        cleaned_data = super(AdminPasswdChangeForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("两次密码输入不一致")


class StructureUpdateForm(forms.ModelForm):
    class Meta:
        model = Structure
        fields = ['type', 'title', 'parent']