from django.urls import path
import cluster.views as views

urlpatterns = [
    path('', views.index, name='index'),
]
