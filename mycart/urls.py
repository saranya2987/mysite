from django.urls import path,include
from . import views
from .views import add_to_cart, cart

app_name = 'mycart'

urlpatterns = [
    path('cart/', cart,name= 'cart'),
    path('cart/add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
#     path('cart/', views.ListCart, name='list-carts'),
#     path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
#     path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
#     path('cart/<int:pk>/update/', views.Updatecart.as_view(), name='update-cart'),
#     path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
]


