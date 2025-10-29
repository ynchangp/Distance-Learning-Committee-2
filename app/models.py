from django.db import models

class Faculty(models.Model):
    korean_name = models.CharField(max_length=100, db_index=True)
    english_name = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

class CourseModality(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    year_semester = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    course_title = models.CharField(max_length=200)
    time_slot = models.CharField(max_length=100, blank=True)
    day = models.CharField(max_length=50, blank=True)
    time = models.CharField(max_length=50, blank=True)
    frequency = models.CharField(max_length=50, blank=True)
    course_format = models.CharField(max_length=100, blank=True)
    reason_for_applying = models.TextField(blank=True)
    modified = models.DateTimeField(auto_now=True)
    apply_this_semester = models.BooleanField(default=False)
    password = models.CharField(max_length=4)
