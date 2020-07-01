from django.shortcuts import render
from .models import *
def base_view(request):
    return render(request,'star/Base.html')

def store_view(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'star/Store.html',context)
