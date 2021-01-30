from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "<a href=\'/rango/about\'>About</a>"
    return HttpResponse(html)

def about(request):
    html = "<a href=\'/rango/\'>Index</a>"
    return HttpResponse(html)