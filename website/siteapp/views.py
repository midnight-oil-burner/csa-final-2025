from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, "siteapp/index.html")
def unit(request, num):
    if num > 10 or num < 1:
        return HttpResponseNotFound("That unit doesn't exist.")
    return render(request, "siteapp/{num}", {"pageNum":num}) #find a way to pass the descriptions stored in some array?