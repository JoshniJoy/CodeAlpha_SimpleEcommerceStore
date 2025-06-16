from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('cart/', views.view_cart, name='view_cart'),
    path('update_item/', views.update_cart_item, name='update_item'),
    path('get_cart_data/', views.get_cart_data_view, name='get_cart_data'),
    path('checkout/', views.checkout, name='checkout'),
    path('profile/<str:username>/', views.user_profile_view, name='profile'),
    path('order-history/', views.order_history_view, name='order_history'),
]