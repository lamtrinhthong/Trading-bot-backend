from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chart.views import CandlestickViewSet

# Initialize the router
router = DefaultRouter()

# Register viewsets with the router
router.register(r'candlesticks', CandlestickViewSet)

# Define the urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart/', include(router.urls)),
]
