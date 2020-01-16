from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:block_height>/', views.block_details, name = 'block_details'),
    path('bhash/<int:previous_hash>/', views.block_hash, name = 'block_hash'),
    path('prices/', views.prices, name = 'prices')
]