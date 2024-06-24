from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandlestickViewSet

router = DefaultRouter()
router.register(r'candlesticks', CandlestickViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
