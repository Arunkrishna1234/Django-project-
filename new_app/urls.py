from django.urls import path

from new_app import views

urlpatterns = [
            path('',views.home,name = "home"),
            path('index',views.index,name ="index"),
            path('kuku',views.kuku,name="kuku"),
            path('customer',views.customer_name,name="customer")


]