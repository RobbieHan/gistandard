# @Time   : 2018/5/6 17:22
# @Author : RobbieHan
# @File   : forms.py


from django import forms
from django.contrib.auth import get_user_model

from .models import WorkOrder, WorkOrderRecord

User = get_user_model()


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'gender', 'birthday', 'email']


class WorkOrderCreateForm(forms.ModelForm):
    # approver = forms.(required=True, error_messages={"required": "请选择审批人"})
    class Meta:
        model = WorkOrder
        fields = '__all__'
        error_messages = {
            "title": {"required": "请输入工单标题"},
            "type": {"required": "请选择工单类型"},
            "status": {"required": "请选择工单状态"},
            "do_time": {"required": "请输入工单安排时间"},
            "content": {"required": "请输入工单内容"},
            "customer": {"required": "请选客户信息"},
        }

    def clean(self):
        cleaned_data = super(WorkOrderCreateForm, self).clean()
        approver = cleaned_data.get("approver", "")
        number = cleaned_data.get("number")
        if not approver:
            raise forms.ValidationError("请选择工单审批人")
        if WorkOrder.objects.filter(number=number).count():
            raise forms.ValidationError("工单编号已存在")


class WorkOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = '__all__'
        error_messages = {
            "title": {"required": "请输入工单标题"},
            "type": {"required": "请选择工单类型"},
            "status": {"required": "请选择工单状态"},
            "do_time": {"required": "请输入工单安排时间"},
            "content": {"required": "请输入工单内容"},
            "customer": {"required": "请选客户信息"},
        }

    def clean(self):
        cleaned_data = super(WorkOrderUpdateForm, self).clean()
        approver = cleaned_data.get("approver", "")
        if not approver:
            raise forms.ValidationError("请选择工单审批人")


class WorkOrderRecordForm(forms.ModelForm):
    class Meta:
        model = WorkOrderRecord
        exclude = ['file_content', ]


class WorkOrderRecordUploadForm(forms.ModelForm):
    class Meta:
        model = WorkOrderRecord
        fields = ['file_content']


class WorkOrderProjectUploadForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ['file_content']
