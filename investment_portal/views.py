from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from userdata.models import userdata
from django.views.decorators.csrf import csrf_protect
from stock.models import transactionhistory
# import json
# import torch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# from .chatbot_assistant import ChatbotAssistant, get_stocks  # Import your chatbot class

# # Load chatbot model
# assistant = ChatbotAssistant('intents.json', function_mappings={'stocks': get_stocks})
# assistant.parse_intents()
# assistant.load_model('chatbot_model.pth', 'dimensions.json')
# from google import genai



# def chatbot_response(request):
#     if request.method == "POST":
#         userinput = request.POST.get('userInput')
#         client = genai.Client(api_key="AIzaSyBfPOZ7vl3kKsIdxM5p89tZpQS6we8vQ6E")
#         response = client.models.generate_content(
#         model="gemini-2.0-flash", contents=userinput
#      )
#         message = response.text
#         return render(request, 'profile.html', {'message': message})
#     return JsonResponse({"error": "Invalid request"}, status=400)

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
     return render(request,'userpro.html')

def stocks(request):
     return render(request,'stocks.html')