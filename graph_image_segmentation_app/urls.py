from . import views
from django.urls import path
from graph_image_segmentation_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploads/', views.upload, name='upload'),
]