from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('account/accountNum/getbalance', views.get_balance, name='get_balance'),
]
