from django.shortcuts import render

# Create your views here.
from .forms import ProductForm

def product_view(request):
    my_context = {
        "my_text": "this is a products context",
        "my_number": 123,
        "my_list": [123, 1, 13, 12, 1234]
    }
    return render(request, "products.html", my_context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product_create.html", context)