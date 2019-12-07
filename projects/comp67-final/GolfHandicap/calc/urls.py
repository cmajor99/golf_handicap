from django.urls import path
from . import views

urlpatterns = [
    path('', views.roundEntry, name='roundEntry'),
]