from django.shortcuts import get_object_or_404, render

from .models import Plot

def index(request):
    latest_plots_list = Plot.objects.order_by('-creation_date')[:5]
    context = {'latest_plots_list': latest_plots_list}
    return render(request, 'tierlists/index.html', context)

def tier_list(request, plots_id):
    plot = get_object_or_404(Plot, pk=plot_id)
    return render(request, 'tierlists/tier_list.html', {'plot': plot})
