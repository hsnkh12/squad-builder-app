from django.contrib import admin
from .models import formations,saved_squad,temp
# Register your models here.

admin.site.register(formations)
admin.site.register(saved_squad)
admin.site.register(temp)