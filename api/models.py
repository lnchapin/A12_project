from django.db import models

# Create your models here.

class Class_Name(models.Model):
    class_id = models.AutoField(primary_key=True, default="")
    class_name = models.CharField(max_length=255, null=True)


class Students(models.Model):
    students_id = models.AutoField(primary_key=True, default="")
    class_id = models.ForeignKey(Class_Name, on_delete=models.CASCADE, null=True)
    class_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=255, null=True)


class Questions(models.Model):
    questions_id = models.AutoField(primary_key=True, default="")
    questions_text = models.CharField(max_length=160, null=True)


class Answers(models.Model):
    students_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=True)
    date_updated = models.DateField(auto_now_add=True, null=True)
    twilio_answer = models.CharField(max_length=160, blank=True, null=True)
    questions_id = models.ForeignKey(Questions, on_delete=models.CASCADE, null=True)
