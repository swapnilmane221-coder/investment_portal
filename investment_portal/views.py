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
  
def main(request):
     if request.method == 'POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('password')
          data=userdata(name=name,email=email,password=password)
          data.save()
          return HttpResponse('login successfully')
     return render(request,'home.html')

