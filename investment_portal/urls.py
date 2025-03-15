
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base),
    path('',views.home),
    path('signup/',views.signup),
    path('main/',views.main,name='main')
]
