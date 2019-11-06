from django.urls import path
from . import views
app_name = "catalog"
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.details, name = 'detail'),
    path('account/', views.getAccount, name = "getAccount")
]
