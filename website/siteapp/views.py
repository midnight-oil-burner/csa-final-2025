from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "siteapp/index.html")
def unit(request, num):
    return render(request, "siteapp/unit.html", {"pageNum":num})