from django.shortcuts import render

from new_app.forms import customerForm
from new_app.models import customer


# Create your views here.
def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def kuku(request):
    form=customer
    return render(request,'kuku.html')
def customer_name(request):
    form=customerForm()

    return render(request,'customer.html',{'form':form})

