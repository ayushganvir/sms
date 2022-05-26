# Generated by Django 4.0.4 on 2022-05-26 09:03
import os, csv
from django.conf import settings
from django.db import migrations


def student_list():
    data_location = os.path.join(settings.BASE_DIR, "data/student.csv")
    with open(data_location) as f:
        csvreader = csv.reader(f)
        rows = []
        for row in csvreader:
            rows.append(row)
    return rows


def add_student_details(apps, schema_editor):
    Student = apps.get_model("sms", "Student")
    for s in student_list():
        Student().save()


class Migration(migrations.Migration):

    dependencies = [
        ("sms", "0003_auto_20220526_0850"),
    ]

    operations = []
