from django.http  import HttpResponse
from cluster.apps import ClusterConfig

def index(request):
    return HttpResponse("Hello")


