from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Plot

class IndexView(generic.ListView):
    template_name = 'tierlists/index.html'
    context_object_name = 'latest_plot_list'

    def get_queryset(self):
        """ Return the last five created plots. """
        return Plot.objects.order_by('-creation_date')[:5]

class PlotView(generic.DetailView):
    model = Plot
    template_name = 'tierlists/plot.html'
