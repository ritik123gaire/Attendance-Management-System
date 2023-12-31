# Generated by Django 4.2.4 on 2023-08-12 20:12

import attendance.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('roll_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('branch', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('CHEM', 'CHEM'), ('MECH', 'MECH'), ('EEE', 'EEE')], max_length=100, null=True)),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=100, null=True)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=attendance.models.student_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, max_length=200, null=True)),
                ('lastname', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to=attendance.models.teacher_directory_path)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('branch', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=200, null=True)),
                ('section', models.CharField(max_length=200, null=True)),
                ('period', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(default='Absent', max_length=200, null=True)),
                ('roll_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.student')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.teacher')),
            ],
        ),
    ]
