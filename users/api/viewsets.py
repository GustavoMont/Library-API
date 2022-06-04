from rest_framework import viewsets
from users.api import serializers
from users import models

class UsersViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializers
    queryset = models.Users.objects.all()