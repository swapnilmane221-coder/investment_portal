
from django.contrib import admin
from django.urls import path
from . import views
# from .views import chatbot_response 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('signup/',views.signup,name='signup'),
    path("profile/",views.profile,name='profile'),
    path('main/',views.main,name='main'),
    path('login/',views.login,name='login'),
    # path("chatbot/", chatbot_response, name="chatbot_response"),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('stocks/',views.stocks,name='stocks'),
]
