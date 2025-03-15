from django.contrib import admin
from stock.models import transactionhistory

class transactionhistoryAdmin(admin.ModelAdmin):
     list_display=['Date','name','amount','quantity','status','total_amount']

admin.site.register(transactionhistory,transactionhistoryAdmin)
# Register your models here.
