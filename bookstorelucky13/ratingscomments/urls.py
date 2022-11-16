from django.urls import path
from ratingscomments import views

urlpatterns = [
    path('ratingscomments/author/', views.author_list),
    path('ratingscomments/author/<int:pk>/', views.author_detail),

    path('ratingscomments/book/', views.book_list),
    path('ratingscomments/book/<int:pk>/', views.book_detail),

    path('ratingscomments/user/', views.user_list),
    path('ratingscomments/user/<int:pk>/', views.user_detail),

    path('ratingscomments/comment/', views.comment_list),
    path('ratingscomments/comment/<int:pk>/', views.comment_detail),

    path('ratingscomments/rating/', views.rating_list),
    path('ratingscomments/rating/<int:pk>/', views.rating_detail),
]