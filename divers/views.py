from django.shortcuts import render
from .models import *
import pandas as pd
import csv




# Create your views here.
def home_page(request):
    return render(request,"divers/homePage.html")

def details_page(request):
    return render(request,"divers/details.html")


def datatable(request):
    csv_fp = open(f'divers/premiere_question.csv', 'r')
    reader = csv.DictReader(csv_fp)
    headers = [col for col in reader.fieldnames]
    out = [row for row in reader]
    return render(request, 'divers/details.html', {'divers' : out, 'headers' : headers})
   
    
