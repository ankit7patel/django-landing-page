from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calls(request):
    return HttpResponse("callss")
