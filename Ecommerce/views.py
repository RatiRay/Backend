from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def EcomPage(request):
    html ="Welcome to my eCommerce page"
    return HttpResponse(html)

    #class based view
# class MyView(View):
#     def get(self,request):
#      return HttpResponse("This is class based view")
