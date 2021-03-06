# Generated by Django 4.0.4 on 2022-05-26 07:47

import os
from django.db import migrations
from django.conf import settings
import csv
import datetime


def book_list():
    data_location = os.path.join(settings.BASE_DIR, "data/book.csv")
    with open(data_location) as f:
        csvreader = csv.reader(f)
        rows = []
        for row in csvreader:
            rows.append(row)
    return rows[1:]


def add_book_details(apps, schema_editor):
    Book = apps.get_model("sms", "Book")
    for title, author, publish_date, num in book_list():
        if publish_date:
            publish_date = datetime.datetime.strptime(publish_date, "%d/%m/%Y").date()
        else:
            publish_date = None
        Book(
            title=title, author=author, publish_date=publish_date, number_of_pages=num
        ).save()


def delete_book_details(apps, schema_editor):
    Book = apps.get_model("sms", "Book")
    books = Book.objects.all()
    books.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("sms", "0001_initial"),
    ]

    operations = [migrations.RunPython(add_book_details, delete_book_details)]
