from django.urls import path
from shoppingcart import views
 
urlpatterns = [
 path('shoppingcart/shoppingcart/', views.shopping_cart_list),
 path('shoppingcart/shoppingcart/<int:pk>/', views.shopping_cart_detail),

]