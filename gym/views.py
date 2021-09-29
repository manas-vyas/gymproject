from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gymsite(request):
    return render(request, 'gymsite.html')