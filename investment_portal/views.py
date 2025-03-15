from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from userdata.models import userdata
from django.views.decorators.csrf import csrf_protect



def base(request):
     return render(request,'base.html')

def home(request):
     return render(request,'home.html')

def signup(request):
     return render(request,'reg.html')
  
def profile(request):
     return render(request,'profile.html')

def main(request):
     if request.method == 'POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          data=userdata(name=name,email=email,password=password)
          data.save()
          return HttpResponseRedirect('/profile')
     return render(request,'home.html')

def login(request):
     if request.method == 'POST':
          email=request.POST.get('email')
          user = userdata.objects.filter(email=email)
          if user[0].password == request.POST.get('password'):
               return HttpResponseRedirect('/profile')
     return render(request,'home.html')