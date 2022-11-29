from django.urls import path,include
from requests import delete
from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView, index, new_one, my_place, product_details, add_product,update_product,delete_product
app_name = 'myapp'

urlpatterns = [
    path('',index),
    path('new/',new_one),
    path('place',my_place),
    # path('products/',products, name='products'),
    path('products/',ProductListView.as_view(), name='products'),
    # path('products/<int:id>',product_details,name='product_details'),
    path('products/<int:pk>',ProductDetailView.as_view(), name='product_details'),
    path('products/add/',add_product,name='add_product'),
    path('products/add/',ProductCreateView.as_view(), name='add_product'),

    path('__reload__/', include('django_browser_reload.urls')),
    # path('products/update/<int:id>',update_product,name='update_product'),
    path('products/update/<int:pk>',ProductUpdateView.as_view(), name='update_product'),

    # path('products/delete/<int:id>',delete_product,name='delete_product'),
    path('products/delete/<int:pk>',ProductDeleteView.as_view(), name='delete_product'),


]