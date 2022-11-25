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
    csv2 = pd.read_csv('divers/ecart_type.csv')
    csv = pd.read_csv('divers/premiere_question.csv')
    csv3 = pd.read_csv('divers/lesbath.csv')
    csv4 = pd.read_csv('divers/quartile_et_autre.csv')
    return render(request, 'divers/details.html', {
        'table' : csv.to_html(classes="center"),
        'tableEcart' : csv2.to_html(classes="center"),
        'tableBath' :csv3.to_html(classes="center"),
        'tableQuart' :csv4.to_html(classes="center")
        
        })


