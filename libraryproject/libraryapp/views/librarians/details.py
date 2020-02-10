# import sqlite3
# from django.urls import reverse
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from libraryapp.models import Book, Library
# from libraryapp.models import model_factory
# from ..connection import Connection


# def get_library(library_id):
#     with sqlite3.connect(Connection.db_path) as conn:
#         conn.row_factory = model_factory(Book)
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#         SELECT
#             lib.id,
#             lib.title,
#             lib.address
#         FROM libraryapp_library lib
#         WHERE lib.id = ?
#         """, (library_id,))

#         return db_cursor.fetchone()

# @login_required
# def book_details(request, library_id):
#     if request.method == 'GET':
#         library = get_library(library_id)

#         template = 'library/details.html'
#         context = {
#             'library': library
#         }

#         return render(request, template, context)