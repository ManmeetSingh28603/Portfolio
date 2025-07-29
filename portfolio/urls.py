from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico', views.favicon, name='favicon'),
    path('favicon.png', views.favicon, name='favicon_png'),
] 