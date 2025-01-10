from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('home/', views.home, name='home'),
    path('home/COORDENADORES/', views.coordenadores, name='home-coordenador'),
    path('home/ADMINISTRADORES/', views.administradores, name='home-adm'),
    path('home/SUPERVISORES/', views.supervisores, name='home-sup'),
]