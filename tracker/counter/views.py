from rest_framework import viewsets
from .serializers import NumberSerializer
from .models  import CounterNumber

class NumberViewSet(viewsets.ModelViewSet):
    queryset = CounterNumber.objects.all()
    serializer_class = NumberSerializer