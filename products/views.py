from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'productsList': products
    }
    return render(request, 'products/index.html', context)