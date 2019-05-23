from django.conf.urls import url
from . import views
                    
urlpatterns = [

    url(r'^$', views.books), #Main Books page
    url(r'^add_book$', views.add_book), #Adding a single book on the Main Books page
    url(r'^books/(?P<book_id>\d+)$', views.view_book), #The page for a single Book
    url(r'^add_auth_to_book/(?P<book_id>\d+)$', views.add_auth_to_book), #Adding an author to a single Book
    url(r'^authors$', views.authors), #Main Authors page
    url(r'^add_author$', views.add_author), #Adding a single author on the Main Authors page
    url(r'^authors/(?P<author_id>\d+)$', views.view_author), #The page for a single Author
    url(r'^add_book_to_auth/(?P<author_id>\d+)$', views.add_book_to_auth) #Adding a book to a single Author
]