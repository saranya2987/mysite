from django.urls import path,include
from requests import delete
from .views import index, new_one, my_place, products, product_details, add_product,update_product,delete_product

app_name = 'myapp'

urlpatterns = [
    path('',index),
    path('new/',new_one),
    path('place',my_place),
    path('products/',products, name='products'),
    path('products/<int:id>',product_details,name='product_details'),
    path('products/add',add_product,name='add_product'),
    path('__reload__/', include('django_browser_reload.urls')),
    path('products/update/<int:id>',update_product,name='update_product'),
    path('products/delete/<int:id>',delete_product,name='delete_product'),


]