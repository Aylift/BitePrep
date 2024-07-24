from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("foods/", views.index, name='index')
]
