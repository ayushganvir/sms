from django.contrib import admin

from .models import Student, School, Book
 
 
@admin.register(Book)
class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'number_of_pages')
 
 
@admin.register(School)
class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('school', 'email', 'principal')
 
 
@admin.register(Student)
class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender')