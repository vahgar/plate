from django.contrib import admin
from .models import BaseUser, ActualUser
# Register your models here.
admin.site.register(BaseUser)
admin.site.register(ActualUser)
