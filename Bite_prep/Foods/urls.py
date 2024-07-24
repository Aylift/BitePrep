from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path("foods_db/", views.foods_db, name='foods_db'),
    path("diary/", views.diary, name='diary'),
]
