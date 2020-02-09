from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('libraries/', libraries_list, name='libraries'),
    path('librarians/', librarians_list, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout')
]