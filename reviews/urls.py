from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/review/', views.product_review, name='product_review'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('add/product/', views.add_product, name='add_product'),
    path('product/', views.product, name='product'),
]