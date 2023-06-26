from django.contrib import admin
from main.models import Home,Latest_Episode,Home_Edit, donation, payment

# Register your models here.

admin.site.register(Home)
admin.site.register(Latest_Episode)
admin.site.register(Home_Edit)
admin.site.register(donation)
admin.site.register(payment)