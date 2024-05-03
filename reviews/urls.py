from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('add/product/', views.add_product, name='add_product'),
    path('product/', views.product, name='product'),

    #new
    path('product/<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/reviews/', views.product_reviews, name='product_reviews'),
    path('products/', views.product_list, name='product_list'),
]