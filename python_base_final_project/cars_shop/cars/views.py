from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def cars_index(request: HttpRequest) -> HttpResponse:
    request = request
    return render(request, template_name="cars/index.html")
