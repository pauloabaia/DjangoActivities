from django.urls import path
from . import views

urlpatterns = [
    path("eco/<str:nome>/", views.HelloViews.eco),
    path("api/", views.HelloViews.api_info),
    path("home/", views.HelloViews.home, name="home"),
    path("contato/", views.HelloViews.contato, name="contato"),
    path("homeT/", views.HelloViews.homeGlobal, name="homeGlobal"),
    path("base/", views.HelloViews.base, name="base"),
]
