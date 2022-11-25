
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page,name ='home'),
    path('details/',views.datatable , name = 'details'),
    path('details2/',views.importImage , name = 'details')
]
  
   

