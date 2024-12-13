from django.urls import path
from .views import course, select, select_student

urlpatterns = [
    path('', course, name = "home"),
    path('course/<int:course_id>/', select, name = 'select'),
    path('student/<int:student_id/>', select_student, name = 'select_student'),
]