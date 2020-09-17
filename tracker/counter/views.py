from rest_framework import viewsets
from .serializers import NumberSerializer, TemSerializer
from .models  import CounterNumber, TemtemName

class NumberViewSet(viewsets.ModelViewSet):
    queryset = CounterNumber.objects.all()
    serializer_class = NumberSerializer

class TemViewSet(viewsets.ModelViewSet):
    queryset = TemtemName.objects.all()
    serializer_class = TemSerializer