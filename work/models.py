
from django.db import models
from datetime import datetime


class Student (models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=400)
    year_of_graduation = models.DateField(default=datetime.today)

    def __str__(self):
        return self.full_name


class School (models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    postal_code = models.IntegerField()
    date = models.DateField(default=datetime.today)

    def __str__(self):
        return self.name


class Certificate (models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True)


    def __str__(self):
        return self.name

class Faculty (models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Department(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    faculty = models.CharField(max_length=700, blank=True)

    def __str__(self):
        return self.name


class Grade (models.Model):
     Student = models.ForeignKey(Student, on_delete=models.CASCADE)
     type = models.CharField(max_length=400, blank=True)

     def __str__(self):
        return self.type




