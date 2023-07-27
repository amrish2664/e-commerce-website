from django.contrib import admin
from django.urls import path
from .views import home, register, user_login, user_logout, add_to_cart, cartItem,payment_product,payment_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home.as_view(), name='home'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('cart/', add_to_cart, name='cart'),
    path('payment/',payment_product,name='payment'),
    path('payment_success',payment_success,name='payment_success'),
    
    
  
]
