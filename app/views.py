from django.shortcuts import render


def home_template(request):
    return render(request, "home.html")
