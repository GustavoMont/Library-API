from tkinter import CASCADE
from django.db import models
from books.models import Books
from users.models import Users

# Create your models here.
class Loans(models.Model):
    book = models.ForeignKey(Books, related_name='book', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name='user', on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
