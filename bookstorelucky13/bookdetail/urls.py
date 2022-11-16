from django.urls import path
from bookdetail import views

urlpatterns = [
    path('bookdetail/author/', views.author_list),
    path('bookdetail/author/<str:pk>/', views.author_detail),

    path('bookdetail/book/', views.book_list),
    path('bookdetail/book/<int:pk>/', views.book_detail),

    path('bookdetail/authorName/', views.book_list_byAuthor),
    path('bookdetail/authorName/<str:AuthorName>/', views.book_detail_byAuthor),
]