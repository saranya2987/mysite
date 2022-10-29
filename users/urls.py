from django.urls import path,include
from .views import register
urlpatterns = [
    # path('',index),
    path('register/',register, name='register'),
    # path('place',my_place),
    # path('products/',products, name='products'),
    # path('products/<int:id>',product_details,name='product_details'),
    

]