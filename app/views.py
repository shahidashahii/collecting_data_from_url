from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good(request,data):
    return HttpResponse(f'Mr/Ms python {data}')