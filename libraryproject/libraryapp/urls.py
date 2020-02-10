from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('libraries/', libraries_list, name='libraries'),
    path('library/form', library_form, name='library_form'),
    path('librarians/', librarians_list, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/<int:book_id>/', book_details, name='book'),
    path('logout/', logout_user, name='logout')
]