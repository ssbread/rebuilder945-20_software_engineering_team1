
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')

def button(request):
    return JsonResponse({"kj":"nb"})