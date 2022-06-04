from rest_framework import viewsets
from books import models
from books.api import serializers

class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializers
    queryset = models.Books.objects.all()