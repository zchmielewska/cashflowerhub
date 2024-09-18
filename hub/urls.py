# hub/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.models_view, name='home'),
    path('models', views.models_view, name='models'),
    path('runs', views.runs_view, name='runs'),
    path('documentation', views.documentation_view, name='documentation'),
]
