from django.contrib import admin
from userdata.models import userdata,compony

class userdataAdmin(admin.ModelAdmin):
     list_display=['name','email','password']
admin.site.register(userdata,userdataAdmin)

class componyAdmin(admin.ModelAdmin):
     list_display=['name','email','password']
admin.site.register(compony,componyAdmin)
# Register your models here.
