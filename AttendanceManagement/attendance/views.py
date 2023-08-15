from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from .models import Teacher, Student, Attendance

def home(request):
    return render(request, 'home.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.student is not None:
            login(request, user)
            return redirect('student_dashboard')  # Redirect to student dashboard
        else:
            messages.error(request, 'Invalid login credentials for student.')
    return render(request, 'student_login.html')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.teacher is not None:
            login(request, user)
            return redirect('teacher_dashboard')  # Redirect to teacher dashboard
        else:
            messages.error(request, 'Invalid login credentials for teacher.')
    return render(request, 'teacher_login.html')

@login_required
def teacher_dashboard(request):
    teacher = request.user.teacher
    students = Student.objects.filter(teacher=teacher)
    attendance_records = Attendance.objects.filter(student__in=students)

    context = {
        'teacher': teacher,
        'students': students,
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher_dashboard.html', context)

@login_required
def student_dashboard(request):
    student = request.user.student
    attendance_records = Attendance.objects.filter(student=student)

    context = {
        'student': student,
        'attendance_records': attendance_records,
    }
    return render(request, 'student_dashboard.html', context)

@staff_member_required
def admin_view(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    attendance_records = Attendance.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
        'attendance_records': attendance_records,
    }
    return render(request, 'admin_view.html', context)

def logout_view(request):
    logout(request)
    return redirect('home') # Redirect to home page
