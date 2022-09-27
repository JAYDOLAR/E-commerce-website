from django.contrib import admin

from productapp.models import categorymodel , productmodel

# Register your models here.
admin.site.register(categorymodel)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','description']
admin.site.register(productmodel,productadmin)