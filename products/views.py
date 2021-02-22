from django.shortcuts import render
from .models import Product
from .forms import ProductForm, PersonForm


def index(request):
    products = Product.objects.all()
    context = {
        'productsList': products
    }
    return render(request, 'products/index.html', context)


def get_product_form(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/getProductForm.html', context)


def get_person_form(request):
    context = {
        'form': PersonForm()
    }
    return render(request, 'products/getPersonForm.html', context)
