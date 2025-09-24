from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse


# Create your views here.
class HelloViews(View):

    def get(self,request):
        return HttpResponse("Hello, my fella! Welcome to my blog")
    
    def eco (request, nome):
        return HttpResponse(f"Hello, dear {nome}!")
    
    def api_info(request):
        data = {"curso": "Django", "nivel":"iniciante"}
        return JsonResponse(data)