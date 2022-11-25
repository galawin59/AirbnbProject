from django.shortcuts import render
from .models import *
import pandas as pd
import csv
from django.http import HttpResponse




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
    csv5 = pd.read_csv('divers/nbhost.csv')
    csv6 = pd.read_csv('divers/nb_review.csv')
    return render(request, 'divers/details.html', {
        'table' : csv.to_html(classes="center"),
        'tableEcart' : csv2.to_html(classes="center"),
        'tableBath' :csv3.to_html(classes="center"),
        'tableQuart' :csv4.to_html(classes="center"),
        'tableNbHost' :csv5.to_html(classes="center"),
        'tableNbReview' :csv6.to_html(classes="center"),
        
        })


def importImage(request):
    img = open("divers/phone.png","rb").read()
    return HttpResponse(img,content_type ="image/png")

