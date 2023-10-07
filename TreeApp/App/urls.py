from django.urls import path
from django.views.generic import TemplateView

from App import views


urlpatterns = [
    path('', views.index),
]