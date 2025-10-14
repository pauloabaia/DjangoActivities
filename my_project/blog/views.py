from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from datetime import date

# Create your views here.
class HelloViews(View):

    def get(self,request):
        return HttpResponse("Hello, my fella! Welcome to my blog")
    
    def eco (request, nome):
        return HttpResponse(f"Hello, dear {nome}!")
    
    def api_info(request):
        data = {"curso": "Django", "nivel":"iniciante"}
        return JsonResponse(data)
    
    def home (request):
        
        contexto = {"nome": "Itallume Apollo",
                    "flag": "is_logged_in",
                    "numero": 10,
                    "numero2" : 20,
                    "now" : date.today,
                    "idade": 18,
                    "role": "vagabundo",
                    "empregados": [
                        {"nome" : "Maria", "cargo": "Engenheira"},
                        {"nome" : "jose", "cargo": "jogador"},
                        {"nome" : "tiago", "cargo": "programador"},
                        {"nome" : "itallo", "cargo": "Engenheiro"},
                        {"nome" : "caio", "cargo": "Médico"}
                                 ],
                        
                     
                     
                      }
        return render(request, "blog/home.html", contexto)
    
    def contato (request):
        return render(request, "blog/contato.html")
    
    def homeGlobal (request):
        return render(request, "global/home.html")
    
    def base (request):
        return render(request, "global/base.html")    