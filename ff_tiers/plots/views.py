from django.shortcuts import get_object_or_404, render

from .models import Plots

def index(request):
    latest_plots_list = Plots.objects.order_by('-creation_date')[:5]
    context = {'latest_plots_list': latest_plots_list}
    return render(request, 'plots/index.html', context)

def tier_list(request, plots_id):
    plot = get_object_or_404(Plots, pk=plots_id)
    return render(request, 'plots/tier_list.html', {'plot': plot})
