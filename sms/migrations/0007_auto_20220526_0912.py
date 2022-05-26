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
    Student = apps.get_model('sms', 'Student')
    School = apps.get_model('sms', 'School')
    Book = apps.get_model('sms', 'Book')
    for id, first_name, last_name, email, gender, school, book in student_list():
        print('>>>', book)
        s = Student(
            first_name = first_name,
            last_name = last_name,
            email = email,
            gender = gender,)
        s.save()
        if school:
            s.school = School.objects.get(school=school)
        if book:  
            b = Book.objects.get(title=book)
            s.books.add(b)
        s.save()


def delete_student_details(apps, schema_editor):
    Student = apps.get_model('sms', 'Student')
    students = Student.objects.all()
    students.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_alter_student_books'),
    ]

    operations = [
        migrations.RunPython(add_student_details, delete_student_details)
    ]
