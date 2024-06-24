from rest_framework import viewsets
from .models.candlestick import Candlestick
from .serializers import CandlestickSerializer

class CandlestickViewSet(viewsets.ModelViewSet):
    queryset = Candlestick.objects.all()
    serializer_class = CandlestickSerializer
