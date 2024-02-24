"""Faculty  URL Configuration 
     Made by me 

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty,name='faculty'),
    path('flogin', views.flogin,name='flogin'),
    path('home', views.home,name='home'),
    path('log_out', views.log_out,name='log_out'),
    path('account', views.account,name='account'),
    path('creat_account', views.creat_account,name='creat_account'),
    path('marks', views.marks,name='marks'),
    path('updated_marks', views.updated_marks,name='updated_marks'),
    path('che_marks', views.che_marks,name='che_marks'),
    

    
]


