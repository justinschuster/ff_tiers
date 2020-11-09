from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def index(request):
    """ View for site index page. """
    return render(request, 'ff_tiers/index.html')