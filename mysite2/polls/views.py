from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(
        request,
        "homepage.html"
    )

def product_list(request):
    products = [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}]

    return render(
        request,
        "product_list.html",
        {
            'products': products
        },
    )

def about_us(request):
    return render(
        request,
        "about_us.html"
    )

def contact(request):
    return render(
        request,
        "contact.html"
    )