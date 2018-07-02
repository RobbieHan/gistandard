# @Time   : 2018/5/24 22:48
# @Author : RobbieHan
# @File   : toolkit.py

import calendar
from datetime import date, timedelta

from django.core.mail import send_mail

from personal.models import WorkOrder
from gistandard.settings import EMAIL_FROM


def get_month_work_order_count(users, value=0):
    """
    生成月度统计工单
    """

    months = range(1, 13)
    filters = dict()
    month_work_order_count = []

    for user in users:
        count = []
        for month in months:
            start_date = date.today().replace(month=month, day=1)
            _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
            end_date = start_date + timedelta(days_in_month)
            if value == 0:
                filters['proposer_id'] = user['id']
            else:
                filters['receiver_id'] = user['id']
            filters['add_time__range'] = (start_date, end_date)
            month_work_order = WorkOrder.objects.filter(**filters).count()
            count.append(month_work_order)
        data = {
            'name': user['name'],
            'count': count
        }
        month_work_order_count.append(data)
    return month_work_order_count


def get_year_work_order_count(users, value=0):
    """
    生成年度统计数据
    """
    filters = dict()
    year_work_order_count = []
    for user in users:
        start_year = date.today().replace(month=1, day=1)
        end_year = date.today().replace(year=(start_year.year + 1), month=1, day=1)
        filters['add_time__range'] = (start_year, end_year)
        if value == 0:
            filters['proposer_id'] = user['id']
        else:
            filters['receiver_id'] = user['id']
        year_work_order = WorkOrder.objects.filter(**filters).count()
        data = {
            'name': user['name'],
            'count': year_work_order
        }
        year_work_order_count.append(data)

    return year_work_order_count


class ToolKit(object):
    '''
    随机生成工单号
    '''

    @classmethod
    def bulidNumber(self, nstr, nlen, srcnum="0"):
        numlen = nlen - len(nstr)
        snum = "1"
        if len(srcnum) == nlen:
            snum = srcnum[len(nstr):len(srcnum)]
            nnum = int(snum)
            snum = str(nnum + 1)
        return nstr + snum.zfill(numlen)


class SendMessage(object):

    @classmethod
    def send_workorder_email(self, number):
        work_order = WorkOrder.objects.get(number=number)
        if work_order.status == "2":
            email_title = u"工单申请通知：{0}".format(work_order.title)
            email_body = """
            {0} 提交了一个新的工单申请， 工单编号 ：{1}， 申请时间：{2}， 安排时间：{3}， 请审批！
            -----------------------------------------------------
            联系人：{4}
            电话 ： {5}
            单位 ： {6}
            地址 ： {7}
            内容 ： {8}
            -----------------------------------------------------
            本邮件为系统通知请勿回复。
            """.format(work_order.proposer.name, work_order.number, work_order.add_time.strftime("%Y-%m-%d %H:%I:%S"),
                       work_order.do_time,
                       work_order.customer.name, work_order.customer.phone, work_order.customer.unit,
                       work_order.customer.address, work_order.content)
            email = [work_order.approver.email, work_order.proposer.email]

        elif work_order.status == "3":
            record = work_order.workorderrecord_set.filter(record_type="1").last()
            email_title = "工单派发通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经派发，申请人：{1}， 申请时间{2}，安排时间{3}，接单人：{4}
            -----------------------------------------------------
            联系人：{5}
            电话 ： {6}
            单位 ： {7}
            地址 ： {8}
            内容 ： {9}
            派发记录：{10}
            -----------------------------------------------------
            本邮件为系统通知请勿回复。
            """.format(work_order.number, work_order.proposer, work_order.add_time.strftime("%Y-%m-%d %H:%I:%S"), work_order.do_time,
                       work_order.receiver,
                       work_order.customer.name, work_order.customer.phone, work_order.customer.unit,
                       work_order.customer.address,
                       work_order.content, record.content)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        elif work_order.status == "4":
            record = work_order.workorderrecord_set.filter(record_type="2").last()
            email_title = "工单执行通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经执行，执行人：{1}
            执行记录：{2}
            本邮件为系统通知请勿回复。
            """.format(work_order.number, work_order.receiver.name, record.content)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        elif work_order.status == "5":
            record = work_order.workorderrecord_set.filter(record_type="3").last()
            email_title = "工单确认通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已经确认完成，确认人：{1}
            确认记录：{2}
            本邮件为系统通知请勿回复。
            """.format(work_order.number, work_order.proposer.name, record.content)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        elif work_order.status == "0":
            record = work_order.workorderrecord_set.filter(record_type="0").last()
            email_title = "工单退回通知：{0}".format(work_order.title)
            email_body = """
            编号为：{0} 的工单已被退回，操作人：{1}
            退回说明：{2}
            本邮件为系统通知请勿回复。
            """.format(work_order.number, record.name.name, record.content)
            email = [work_order.approver.email, work_order.proposer.email, work_order.receiver.email]

        send_status = send_mail(email_title, email_body, EMAIL_FROM, email)
        if send_status:
            pass
