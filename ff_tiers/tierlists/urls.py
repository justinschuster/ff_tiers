from django.urls import path

from . import views

app_name = 'tierlists'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PlotView.as_view(), name='plot'),
]
