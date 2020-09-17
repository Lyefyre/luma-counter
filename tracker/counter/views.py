from rest_framework import viewsets
from .serializers import NumberSerializer
from .models  import CounterNumber
from rest_framework.decorators import action
from rest_framework.response import Response

class NumberViewSet(viewsets.ModelViewSet):
    """
    This viewset provides list, create, retrieve, update and destroy actions.
    """
    queryset = CounterNumber.objects.all()
    serializer_class = NumberSerializer