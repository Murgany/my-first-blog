from django.shortcuts import render
from .models import *

# market view to render products from data base.


def market(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})


# base view from which we will inherit navbar for multiple templates
def base(request):
    context = {}
    return render(request, 'base.html', context)



