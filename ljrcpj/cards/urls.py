from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('rookie-cards/<slug:slug>/', views.card, name='slugs'),
    path('rookie-cards', views.cardsall, name='slugss'),

]