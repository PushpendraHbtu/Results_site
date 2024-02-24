"""result URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header='RESULT ADMIN PANEL'
admin.site.site_title='Online Result'
admin.site.site_header='Welcome to Online Result Site'



urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('Faculty/', include('faculty.urls')),
    path('student/', include('student.urls')),
]
