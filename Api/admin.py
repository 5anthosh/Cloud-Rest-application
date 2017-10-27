from django.contrib import admin
from .models import Field, Channel, FieldHistory
#from rest_framework.authtoken.models import Token

admin.site.register(Field)
admin.site.register(Channel)
admin.site.register(FieldHistory)
# Register your models here.
