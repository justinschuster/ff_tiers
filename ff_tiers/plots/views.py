from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def tier_list(request, plots_id):
    return HttpResponse("ur looking at a plot %s" % plots_id)
