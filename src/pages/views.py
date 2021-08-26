from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home.html", context)

def about_view(request):
    context = {}
    return render(request, 'about.html', context)

def contact_view(request):
    context = {}
    return render(request, 'contact.html', context)

def error_view(request, template_name='500.html'):
    context = {}
    return render(request, template_name, context)

def page_not_found_view(request, exception, template_name='404.html'):
    context = {}
    return render(request, template_name, context)