import sys
import os

import csv

pwd = (os.path.dirname(os.path.realpath(__file__)))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gistandard.settings")

import django
django.setup()
from django.contrib.auth import get_user_model
from adm.models import Customer

User = get_user_model()




customers_list = []
with open('data/customer_data.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        belongs_to = User.objects.get(name=row[1])
        data = {
            "unit": row[0],
            "address": "未添加",
            "name": "未添加",
            "phone": "未添加",
            "belongs_to": belongs_to,
            "status": True
        }
        customers_list.append(data)

for customer in customers_list:
    cus_intance = Customer()
    cus_intance.unit = customer["unit"]
    cus_intance.address = customer["address"]
    cus_intance.name = customer["address"]
    cus_intance.phone = customer["phone"]
    cus_intance.belongs_to = customer["belongs_to"]
    cus_intance.status = customer["status"]
    cus_intance.save()
