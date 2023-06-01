from django.shortcuts import render


# Create your views here.
def browser(request):
    return render(request, "browser/main.html", {})
