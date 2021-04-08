from django.urls import path
from . import views


urlpatterns = [
              path('', views.market, name='home'),
              path('base/', views.base, name='base'),
]