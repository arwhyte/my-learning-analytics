# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-11 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='enrollment_type',
            field=models.CharField(blank=True, choices=[('StudentEnrollment', 'Student'), ('TaEnrollment', 'Teaching Assistant'), ('TeacherEnrollment', 'Instructor')], max_length=50, null=True, verbose_name='Enrollment Type'),
        ),
    ]