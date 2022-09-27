from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_books),
    path('add_book/', views.add_book),
    path('books/<int:book_id>/', views.show_book),
    path('books/<int:book_id>/add_author/', views.add_author_to_book),
    path('authors/', views.index_authors),
    path('authors/add_author/', views.add_author),
    path('authors/<int:author_id>/', views.show_author),
    path('authors/<int:author_id>/add_book/', views.add_book_to_author),
]