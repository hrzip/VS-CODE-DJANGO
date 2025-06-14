from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def home (request):
    posts = Post.objects.order_by("time")
    return render(request, "home.html", {"posts":posts})


def about (request):
    podaci = {"Ime":"pero", "Prezime":"peric", "Telefon":"0991900000"}

    return render(request, "about.html", podaci)
