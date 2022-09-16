from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def kiyimlar(request):
    return render(request,'messages.html')