from rest_framework import viewsets
from loans.api import serializers
from loans import models


class LoansViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoansSerializers
    queryset = models.Loans.objects.all()