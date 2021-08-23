from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
#this is where all the views go for the app/component products

def products_view(request):
    my_context = {
        "my_text": "this is a products context",
        "my_number": 123,
        "my_list": [123, 1, 13, 12, 1234]
    }
    return render(request, "products.html", my_context)
