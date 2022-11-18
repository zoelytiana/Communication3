"""Communication URL Configuration

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
from django.urls import path
from django.views.defaults import server_error
from .views import index, messageDetail, envoyerMessage, addRequest, saveRequest, validRequest, refuseRequest, logOut

urlpatterns = [
    path('', index, name="message"),
    path('<int:id>', messageDetail),
    path('add/', addRequest),
    path('message/save/', saveRequest, name="saveRequest"),
    path('valid/<int:id>', validRequest),
    path('refuse/<int:id>', refuseRequest),
    path('logout/', logOut),
]
