from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /plots/2
    path('<int:plots_id>/', views.tier_list, name='tier_list'),
]
