from django.shortcuts import render, redirect
from .forms import BookForm, QueryForm, SchoolForm, StudentForm
from .models import Student
from django.contrib import messages


def index(request):
    if request.GET:
        form = QueryForm(request.GET)
        if form.is_valid():
            students = form.search()
            return render(
                request, "sms/index.html", {"students": students, "form": form}
            )
    else:
        form = QueryForm()
    return render(request, "sms/index.html", context={"form": form})


def create_student(request):
    if request.POST:
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid():

            form.save()
            messages.success(request, "Student Successfully Added")
        else:
            messages.error(request, "Error saving form")
        return redirect("index")
    form = StudentForm()
    return render(request, "sms/create_student.html", context={"form": form})


def create_school(request):
    if request.POST:
        form = SchoolForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "School Successfully Added")
        else:
            messages.error(request, "Error saving form")
        return redirect("index")
    form = SchoolForm()
    return render(request, "sms/create_school.html", context={"form": form})


def create_book(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, "Book Successfully Added")
        else:
            messages.error(request, "Error saving form")
        return redirect("index")
    form = BookForm()
    return render(request, "sms/create_book.html", context={"form": form})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, "sms/student_detail.html", context={"student": student})
