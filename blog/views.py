from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Welcome to the Blog!")
    return render(request, 'blog/home.html')