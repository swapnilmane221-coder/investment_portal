from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from userdata.models import userdata
from django.views.decorators.csrf import csrf_protect
from stock.models import transactionhistory


def base(request):
     return render(request,'base.html')

def home(request):
     return render(request,'home.html')

def signup(request):
     return render(request,'reg.html')
  
def profile(request):
     stocktransdata=transactionhistory.objects.all()
     total=0
     pending_inv=0
     for i in stocktransdata:
          if i.status == 'pending':
               pending_inv+=i.total_amount
          total+=i.total_amount
     completed_inv=total-pending_inv
     data={'total':total,'stocktransdata':stocktransdata,'pending_inv':pending_inv,'completed_inv':completed_inv}


     return render(request,'profile.html',data)

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