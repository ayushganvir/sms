# Generated by Django 4.0.4 on 2022-05-26 08:50
from django.conf import settings
from django.db import migrations
import os, csv

from sms.models import School

def school_list():
    data_location = os.path.join(settings.BASE_DIR, "data/school.csv")
    with open(data_location) as f:
        csvreader = csv.reader(f)
        rows = []
        for row in csvreader:
            rows.append(row)
    return rows[1:]

def add_school_details(apps, schema_editor):
    School = apps.get_model('sms', 'School')
    for region_id, school, email, principal, phone_no, address in school_list():
        School(
            region_id = region_id,
            school = school,
            email = email,
            principal = principal,
            phone_no = phone_no,
            address = address,
        ).save()

def delete_school_details(apps, schema_editor):
    School = apps.get_model('sms', 'School')
    schools = School.objects.all()
    schools.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20220526_0747'),
    ]

    operations = [
        migrations.RunPython(add_school_details, delete_school_details)
    ]
