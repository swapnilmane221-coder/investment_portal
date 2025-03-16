
from django.contrib import admin
from django.urls import path
from . import views
from .views import  get_insurance_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('signup/',views.signup,name='signup'),
    path("profile/",views.profile,name='profile'),
    path('main/',views.main,name='main'),
    path('login/',views.login,name='login'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('stocks/',views.stocks,name='stocks'),
    path('insurance/', views.insurance, name='insurance'),
    path('api/data/', get_insurance_data, name='get_insurance_data'),
    path('freq/',views.freq,name='freq'),
    path('bonds/',views.bonds,name='bonds'),
    path('stock_view',views.stock_view,name='stock_view'),
    path('chatbot',views.chatbot,name='chatbot'),
]
