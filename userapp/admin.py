from django.contrib import admin

from userapp.models import usermodel

# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display = ['name','email','contact']
    list_filter = ['contact','email']
admin.site.register(usermodel,useradmin)