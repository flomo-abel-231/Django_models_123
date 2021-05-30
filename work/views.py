
from django.shortcuts import render
from django.http import HttpResponse
from . models import Student,School,Grade,Certificate,Faculty,Department

def home(request):
    student = Student.objects.get(id=5)
    return HttpResponse(student)