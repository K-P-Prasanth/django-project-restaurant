from django.contrib import admin
from .models import User,Item,Order,Sale,Category
# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Sale)
