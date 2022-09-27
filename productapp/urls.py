from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview , name='home'),
    path('product/', views.productview , name='product'),
    path('logout', views.logoutview , name='logout')
]