from django.urls import path
from . import views
app_name = "catalog"
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.details, name = 'detail'),
    path('getAccountWith/', views.getAccountToWithdrawal, name = 'getAccountToWithdrawal'),
    path('getAccountView/', views.getAccountToView, name = "getAccountToView"),
    path('getAccountTransfer', views.getAccountToTransfer, name = "getAccountToTransfer"),
    path('transfer/', views.transfer, name = "transfer"),
    path('withdraw/', views.withdraw, name = "withdraw"),
]
