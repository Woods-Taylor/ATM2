from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('account/<uuid:pk>/get_balance/', views.get_balance, name='get_balance'),
]
