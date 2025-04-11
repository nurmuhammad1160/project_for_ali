from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify_spravka, name='verify_spravka'),
    path('sprafkalar/', views.spravka_list, name='spravka_list'),
    path('sprafka/add/', views.spravka_create, name='spravka_create'),
    path('sprafka/<int:pk>/edit/', views.spravka_update, name='spravka_update'),
    path('sprafka/<int:pk>/delete/', views.spravka_delete, name='spravka_delete'),
]

