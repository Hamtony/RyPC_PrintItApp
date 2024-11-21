from django.urls import path
from . import views

urlpatterns = [
   path('registro/', views.registro, name='registro'),
   path('login/', views.login_view, name='login'),
   path('inicio/', views.inicio, name='inicio'),
   path('solicitar_encargo/', views.solicitar_encargo, name='solicitar_encargo'),
   path('', views.landing_page, name='landing_page'),
]
