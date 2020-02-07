from .library import Library
from .librarian import Librarian


from django.db import models

    class Book(module.Models):
        Title = models.CharField(max_length=50)
        ISBN_number = models.CharField(max_length=50)
        Author = models.CharField(max_length=50)
        Year_published = models.IntegerField(_(""))
        location = models.ForeignKey(Library, on_delete=models.CASCADE)
        librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
