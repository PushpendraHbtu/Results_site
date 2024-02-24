"""Students  URL Configuration 
     Made by me 

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student,name='student'),
    path('slogin', views.slogin,name='slogin'),
    path('shome', views.shome,name='shome'),
    path('slog_out', views.slog_out,name='slog_out'),
    path('smarks', views.smarks,name='smarks'),
    
    

    
]


