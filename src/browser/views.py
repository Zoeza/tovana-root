from django.shortcuts import render


# Create your views here.

def home (request):
    return render(request, "browser/main.html", {})

def browser(request):
    return render(request, "browser/browser.html", {})
