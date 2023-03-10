from django.urls import path

from .views import AuthorCreateView, AuthorDeleteView, AuthorDetailView, AuthorListView, AuthorUpdateView, \
    author_detail, author_list, book_detail, book_list, book_list_cache, index, publisher_detail, publisher_list, \
    store_detail, store_list

urlpatterns = [
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('store/<int:store_id>/', store_detail, name='store_detail'),
    path('publisher/<int:publisher_id>/', publisher_detail, name='publisher_detail'),
    path('booklist', book_list, name='book_list'),
    path('authorlist', author_list, name='author_list'),
    path('publisherlist', publisher_list, name='publisher_list'),
    path('storelist', store_list, name='store_list'),
    path('', index, name='index'),

    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    path('booklist_cache', book_list_cache, name='book_list_cache'),
]
