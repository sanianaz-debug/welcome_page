from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # 👈 rendering template


def pricing(request):
    return render(request, "pricing.html")

def contact(request):
    return render(request, "contact.html")

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")

def refund(request):
    return render(request, "refund.html")

def shipping(request):
    return render(request, "shipping.html")
