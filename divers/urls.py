
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('details/',views.details_page)

]
