from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Страница приложения women.")


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")
