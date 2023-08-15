from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    branch = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    # Add any other fields you need

    # Provide unique related_name attributes for the reverse relations
    groups = None
    user_permissions = None

    class Meta:
        unique_together = ("branch",)  # Optional: If you want branch to be unique

    def __str__(self):
        return self.username

def teacher_directory_path(instance, filename):
    name, ext = filename.split(".")
    name = instance.user.username
    filename = name + '.' + ext
    return 'teacher_images/{}/{}/{}'.format(instance.user.branch, instance.user.year, filename)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    teacher_id = models.CharField(primary_key=True, max_length=10)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=teacher_directory_path, null=True, blank=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return str(self.firstname + " " + self.lastname)

def student_directory_path(instance, filename):
    # Split the filename by the last period to handle filenames with multiple periods
    name, ext = filename.rsplit('.', 1)
    name = instance.roll_no
    filename = f"{name}.{ext}"
    return 'student_images/{}/{}/{}/{}'.format(instance.branch, instance.year, instance.section, filename)


class Student(models.Model):
    BRANCH = (
        ('CSE', 'CSE'),
        ('IT', 'IT'),
        ('ECE', 'ECE'),
        ('CHEM', 'CHEM'),
        ('MECH', 'MECH'),
        ('EEE', 'EEE'),
    )
    YEAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    SECTION = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    roll_no = models.CharField(primary_key=True, max_length=20)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    year = models.CharField(max_length=100, null=True, choices=YEAR)
    section = models.CharField(max_length=100, null=True, choices=SECTION)
    image = models.ImageField(upload_to=student_directory_path)

    def __str__(self):
        return str(self.roll_no)

class Attendance(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    branch = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=200, null=True)
    section = models.CharField(max_length=200, null=True)
    period = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, default='Absent')

    def __str__(self):
        return str(self.roll_no) + "_" + str(self.date) + "_" + str(self.period)
