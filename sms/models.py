from django.db import models


class School(models.Model):
    region_id = models.IntegerField(default=100)
    school = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    principal = models.CharField(max_length=30, blank=False)
    phone_no = models.CharField(max_length=8, blank=False)
    address = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.school


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, default="")
    author = models.CharField(max_length=80, blank=True)
    publish_date = models.DateField(blank=True, null=True)
    number_of_pages = models.IntegerField(blank=False, default=100)

    def __str__(self):
        return self.title


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=250, blank=False, default="")
    gender = models.CharField(max_length=20, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.first_name
