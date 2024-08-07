from django.shortcuts import render, redirect

from new_app.forms import CustomerForm, CustomerForm
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
    form=CustomerForm()
    if request.method == 'POST':
        data = CustomerForm(request.POST)
        if data.is_valid():
            data.save()

    return render(request,'customer.html',{'form':form})
def viewcustomer(request):
    data = customer.objects.all()
    return render(request,'view_data.html',{'data':data})
def customer_delete(request,id):
    data = customer.objects.get(id=id)
    data.delete()
    return redirect("viewcustomer")
def customer_update(request,id):
    data = customer.objects.get(id=id)
    form = CustomerForm(instance = data)
    if request.method == 'POST':
        data = CustomerForm(request.POST)
        if data.is_valid():
            data.save()
            return  redirect("customer_view")
    return render(request,'update.html',{'form':form})





