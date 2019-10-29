from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cards/', views.AccountListView.as_view(), name='cards'),
]
