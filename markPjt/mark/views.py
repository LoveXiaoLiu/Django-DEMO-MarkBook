from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    if request != '' and request.method == 'POST':
        data = request.POST
    return HttpResponse('ok')