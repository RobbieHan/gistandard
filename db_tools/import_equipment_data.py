import sys
import os

import csv

pwd = (os.path.dirname(os.path.realpath(__file__)))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gistandard.settings")

import django
django.setup()
from django.contrib.auth import get_user_model
from adm.models import Customer, EquipmentType, Equipment

User = get_user_model()

equipments = []
with open('data/equipment_data.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:

        equipment_type = EquipmentType.objects.filter(name=row[2])
        customer = Customer.objects.filter(unit=row[3])
        data = {
            "number": row[0],
            "equipment_type": equipment_type[0],
            "equipment_model": row[1],
            "buy_date": row[5],
            "warranty_date": row[6],
            "customer": customer[0]
        }
        equipments.append(data)
for equipment in equipments:
    equ_intance = Equipment()
    equ_intance.number = equipment["number"]
    equ_intance.equipment_type = equipment["equipment_type"]
    equ_intance.equipment_model = equipment["equipment_model"]
    equ_intance.buy_date = equipment["buy_date"]
    equ_intance.warranty_date = equipment["warranty_date"]
    equ_intance.customer = equipment["customer"]
    equ_intance.save()




