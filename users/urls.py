from django.urls import path,include
from .views import register,profile,createprofile,seller_profile
from django.contrib.auth import views as authentication_views

app_name = 'users'

urlpatterns = [
    path('register/',register, name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',profile, name='profile'),
    path('createprofile/',createprofile, name='createprofile'),
    path('sellerprofile/<int:id>',seller_profile, name='sellerprofile'),

   

]