from django.urls import path
from . import views

urlpatterns = [
    path('', views.ModelListView.as_view(), name='home'),

    # Model
    path('model', views.ModelListView.as_view(), name='model_list'),
    path('model/add/', views.ModelCreateView.as_view(), name='model_add'),
    path('model/<int:pk>/', views.ModelDetailView.as_view(), name='model_detail'),
    path('model/edit/<int:pk>/', views.ModelUpdateView.as_view(), name='model_edit'),
    path('model/delete/<int:pk>/', views.ModelDeleteView.as_view(), name='model_delete'),

    # Run
    path('run', views.run_view, name='run'),

    # Document
    path('document/', views.DocumentListView.as_view(), name='document_list'),
    path('document/add', views.DocumentCreateView.as_view(), name='document_add'),
    path('document/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('document/edit/<int:pk>/', views.DocumentUpdateView.as_view(), name='document_edit'),
    path('document/delete/<int:pk>/', views.DocumentDeleteView.as_view(), name='document_delete'),
]
