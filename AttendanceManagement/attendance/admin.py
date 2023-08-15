from django.contrib import admin
from .models import Teacher, Student, Attendance, CustomUser

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)

