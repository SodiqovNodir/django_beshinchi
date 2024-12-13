from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from .models import Course, Student

def course(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    contexts = {
        'courses' : courses,
        'students' : students
    }
    return render(request, 'index.html', context = contexts)

def select(request, course_id):
    courses = Course.objects.all()
    students = Student.objects.filter(course = course_id)

    contexts = {
        'courses' : courses,
        'students' : students,
    }
    return render(request, "index.html", context = contexts)

def select_student(request, student_id):
    courses = Course.objects.all()
    students = Student.objects.filter(student = student_id)
    contexts = {
        'courses' : courses,
        'students' : students,
    }
    return render(request, "index.html", context = contexts)

