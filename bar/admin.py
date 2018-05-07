from django.contrib import admin
from .models import Staff, Waiter, Orders,Items,Categories

# Register your models here.

admin.site.register(Staff)
admin.site.register(Categories)
admin.site.register(Waiter)
admin.site.register(Orders)
admin.site.register(Items)