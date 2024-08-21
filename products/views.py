from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# /products ->index
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
    # return HttpResponse('Hello World')
def new_product(request):
    return HttpResponse('new product')