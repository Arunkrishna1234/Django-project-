from django.urls import path

from new_app import views

urlpatterns = [
            path('',views.home,name = "home"),
            path('index',views.index,name ="index"),
            path('kuku',views.kuku,name="kuku"),
            path('customer',views.customer_name,name="customer"),
            path('viewcustomer',views.viewcustomer,name="viewcustomer"),
            path('customer_delete/<int:id>/',views.customer_delete,name='customer_delete'),
            path('customer_update/<int:id>/',views.customer_update,name='customer_update')

]