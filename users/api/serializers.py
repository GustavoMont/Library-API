from dataclasses import fields
from rest_framework import serializers
from users import models


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'