from django.db import models

# Create your models here.

class Class_Name(models.Model):
    class_id = models.CharField(max_length=255, primary_key=True)
    class_name = models.CharField(max_length=255)


class Students(models.Model):
    students_id = models.CharField(max_length=255, primary_key=True),
    class_id = models.ForeignKey(Class_Name, on_delete=models.CASCADE),
    class_name = models.CharField(max_length=255),
    first_name = models.CharField(max_length=255),
    last_name = models.CharField(max_length=255),
    phone = models.CharField(max_length=12),
    email = models.CharField(max_length=255)


class Questions(models.Model):
    questions_id = models.CharField(max_length=255, primary_key=True),
    questions_text = models.CharField(max_length=160)


class Answers(models.Model):
    students_id = models.ForeignKey(Students, on_delete=models.CASCADE),
    date_updated = models.DateField(auto_now_add=True),
    twilio_answer = models.CharField(max_length=160, blank=True),
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
