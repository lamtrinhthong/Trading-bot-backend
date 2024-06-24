from rest_framework import serializers
from .models.candlestick import Candlestick

class CandlestickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candlestick
        fields = '__all__'
