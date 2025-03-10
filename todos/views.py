from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("<h1>리퀘스트입</h1>")
    return render(request, "home.html")
