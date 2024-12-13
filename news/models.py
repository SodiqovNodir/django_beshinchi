from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='course/photo', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    enrolled_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='student/photo', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
