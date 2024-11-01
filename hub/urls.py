from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_view, name='home'),
    path('model', views.model_view, name='model'),
    path('model/<int:pk>/', views.ModelDetailView.as_view(), name='model_detail'),
    path('model/add', views.model_add, name='model_add'),
    path('models/edit/<int:model_id>/', views.model_edit, name='model_edit'),
    path('model/delete/<int:model_id>/', views.model_delete, name='model_delete'),
    path('run', views.run_view, name='run'),
    path('document', views.document_view, name='document'),
]
