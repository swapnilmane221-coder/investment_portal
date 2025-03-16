from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from userdata.models import userdata
from django.views.decorators.csrf import csrf_protect
from stock.models import transactionhistory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import razorpay
from django.conf import settings
import json

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = data.get("amount")  # Amount in paise (1 INR = 100 paise)

            # Create order
            razorpay_order = razorpay_client.order.create({
                "amount": amount,  # Amount should be in the smallest currency unit (paise)
                "currency": "INR",
                "payment_capture": 1  # Auto capture payment
            })

            return JsonResponse({"id": razorpay_order["id"], "amount": razorpay_order["amount"], "currency": "INR"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

id=userdata.objects.get(email='sahil09@gmail.com').id

def insurance(request):
    return render(request, "insurance.html")

def get_insurance_data(request):
    api_url = "https://api.example.com/insurance/list?token=dYkhLKCmzrr1SPSb2dwtUE8AHUDdE4Cr"
    response = requests.get(api_url)
    data = response.json() if response.status_code == 200 else []
    return JsonResponse(data, safe=False)

def home(request):
     return render(request,'home.html')

def signup(request):
     return render(request,'reg.html')
  
def profile(request):
     stocktransdata=transactionhistory.objects.all()
     total=0
     pending_inv=0
     for i in stocktransdata:
          if i.status == 'sell':
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
          msg=None
          try:
               user = userdata.objects.filter(email=email)
               if user[0].password == request.POST.get('password'):
                    msg=None
                    id=userdata.objects.get(email=email).id
               else:
                    msg='Invalid Credentials'
          except:
               msg='Invalid Credentials'
          if msg=='':
               return HttpResponseRedirect('/profile')
          else:
               return render(request,'reg.html',{'msg':msg})
     return render(request,'reg.html')

def userprofile(request):
     name=userdata.objects.get(id=id).name
     return render(request,'userpro.html',{'name':name})

def stocks(request):
     return render(request,'stocks.html')

def freq(request):
     return render(request,'freq.html')

def bonds(request):
     return render(request,'bonds.html')

def stock_view(request):
     return render(request,'stock_view.html')

def chatbot(request):
     return render(request,'chatbot.html')