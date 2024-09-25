from django.urls import path
from . import views
from .views import delete_diary_record, delete_food_record


urlpatterns = [
    path('', views.home, name='home'),
    path("foods_db/", views.foods_db, name='foods_db'),
    path("diary/", views.diary, name='diary'),
    path('delete-food/<int:pk>/', delete_diary_record, name='delete_diary_record'),
    path('delete/<int:pk>/', delete_food_record, name='delete_food_record'),

]
