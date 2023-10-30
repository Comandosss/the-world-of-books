from django.urls import path

from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/<int:pk>/', views.book_detail, name='details'),
    path('books/', views.books_list, name='books'),
]
