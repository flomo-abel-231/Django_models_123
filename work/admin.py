from django.contrib import admin
from . models import Student, School, Certificate, Grade, Faculty, Department

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Grade)
admin.site.register(Certificate)
admin.site.register(Faculty)
admin.site.register(Department)