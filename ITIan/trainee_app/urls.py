from django.urls import path
from . import views

urlpatterns = [
    path('', views.trainee_list, name='trainee_list'),
]