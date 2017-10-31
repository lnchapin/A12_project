from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Students

# Create your views here.
def index(request):
    return HttpResponse("Hello, it's me")

def students(request):
    allStudents = serializers.serialize("json", Students.objects.all())
    return HttpResponse(allStudents)
