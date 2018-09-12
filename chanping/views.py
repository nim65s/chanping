from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'chanping/index.html', {})


def ping(request):
    d = {'pong': request.GET['ping']}
    return JsonResponse(d)
