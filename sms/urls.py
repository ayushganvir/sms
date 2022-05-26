from django.urls import path

from . import views

urlpatterns = [
    path('<int:student_id>/', views.detail, name='student_detail'),
    path('create_student', views.create_student, name='create_student'),
    path('create_school', views.create_school, name='create_school'),
    path('create_book', views.create_book, name='create_book'),
    path('', views.index, name='index'),
]