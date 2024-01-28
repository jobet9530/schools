from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  school = models.CharField(max_length=100)
  grade = models.IntegerField()
  grade_level = models.CharField(max_length=100)
  enrollment_date = models.DateField()
  graduation_date = models.DateField()
  is_active = models.BooleanField(default=True)
  