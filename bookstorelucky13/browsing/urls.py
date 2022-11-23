from django.urls import path
from browsing import views

urlpatterns = [
    path('browsing/author/', views.author_list),
    path('browsing/author/<int:pk>/', views.author_detail),

    path('browsing/book/', views.book_list),
    path('browsing/book/<int:pk>/', views.book_detail),
    path('browsing/genre/<str:feature>/',views.genre),
    path('browsing/top_seller/',views.top_seller),
    path('browsing/rating/<int:feature>/',views.rating),
    path('browsing/position/<int:feature>/<int:pk>/',views.position),
]