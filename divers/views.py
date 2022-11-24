from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request,"divers/homePage.html")

def details_page(request):
    return render(request,"divers/details.html")