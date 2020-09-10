from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("Hello world!!!!!!")

def home(request):
     params={'name':'siddharth','age':23}
     return render(request,'home.html')

# def about(request):
#     return HttpResponse("this is about page")


def new_page(request):
    data = request.GET["fulltextarea"]
    return render(request, 'newpage.html',{'data':data})
