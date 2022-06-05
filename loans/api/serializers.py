from dataclasses import fields
from rest_framework import serializers
from loans import models


class LoansSerializers(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field='book', read_only=True)
    name = serializers.SlugRelatedField(slug_field='user', read_only=True)
    class Meta:
        model = models.Loans
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = instance.user.name
        response['book'] = instance.book.title
        return response