from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexPageView.as_view(), name="main_page"),
]
