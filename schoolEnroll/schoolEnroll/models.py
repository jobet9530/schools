from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
  student_no = models.IntegerField(),
  student_id = models.CharField(max_length=10, unique=True),
  first_name = models.CharField(max_length=255),
  last_name = models.CharField(max_length=255),
  gender = models.CharField(max_length=20),
  date_of_birth = models.DateField(),
  address = models.CharField(max_length=255),
  phone_number = models.CharField(max_length=20),
  email = models.EmailField(),
  user = models.OneToOneField(User, on_delete=models.CASCADE),

  class Meta:
    abstract = True


class Teacher(models.Model):
  teacher_id = models.CharField(max_length=10, unique=True),
  first_name = models.CharField(max_length=255),
  last_name = models.CharField(max_length=255),
  gender = models.CharField(max_length=20),
  date_of_birth = models.DateField(),
  address = models.CharField(max_length=255),
  phone_number = models.CharField(max_length=20),
  email = models.EmailField(),
  user = models.OneToOneField(User, on_delete=models.CASCADE),

  class Meta:
    abstract = True

class Enrollments(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE),
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE),
  grade = models.IntegerField(),
  class_name = models.CharField(max_length=255),
  date_enrolled = models.DateField(),
  date_completed = models.DateField(),
  user = models.ForeignKey(User, on_delete=models.CASCADE),

  class Meta:
    abstract = True

class Subject(models.Model):
  subject_name = models.CharField(max_length=255),
  subject_code = models.CharField(max_length=10),
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE),
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  class Meta:
    abstract = True

class Class(models.Model):
  class_name = models.CharField(max_length=255),
  class_code = models.CharField(max_length=10),
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE),
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    abstract = True

class Section(models.Model):
  section_name = models.CharField(max_length=255),
  section_code = models.CharField(max_length=10),
  class_name = models.ForeignKey(Class, on_delete=models.CASCADE),
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  class Meta:
    abstract = True