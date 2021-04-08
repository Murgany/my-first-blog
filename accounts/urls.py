from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('password_reset/', views.password_reset_form, name='password_reset_form'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('password_reset_confirm/', views.password_reset_confirm, name='password_reset_confirm')
]