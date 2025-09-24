from django.urls import path
from . import views

urlpatterns = [
    path("eco/<str:nome>/", views.HelloViews.eco),
    path("api/", views.HelloViews.api_info),
]
