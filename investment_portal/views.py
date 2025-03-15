from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def base(request):
     return render(request,'base.html')

def home(request):
     return render(request,'home.html')

def signup(request):
     return render(request,'reg.html')

def profile(request):
     return render(request,'profile.html')