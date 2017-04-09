from django.shortcuts import render,HttpResponse,

# Create your views here.
def login(request):
    html_content = "hello django."
    return HttpResponse(html_content)
def article(request,year,month,id):
    html = "ddd"
    return HttpResponse(html)
def index(request):
    return HttpResponse