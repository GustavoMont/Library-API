from rest_framework import serializers
from loans import models
from exceptions.books import NoBook
from books.models import Books

class LoansSerializers(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field='book', read_only=True)
    name = serializers.SlugRelatedField(slug_field='user', read_only=True)
    class Meta:
        model = models.Loans
        fields = '__all__'
    def create(self, validated_data):
        book = Books.objects.filter(pk=validated_data['book'].id)
        book_quantity = book.values()[0]['quantity'] 
        if book_quantity <= 0:
            raise NoBook()
        book.update(quantity=book_quantity-1)
        return super().create(validated_data)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = instance.user.name
        response['book'] = instance.book.title
        return response