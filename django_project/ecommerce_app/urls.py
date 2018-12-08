from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>/',
        views.show_product, name='product_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
]