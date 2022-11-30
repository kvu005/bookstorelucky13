from rest_framework.routers import DefaultRouter
from django.urls import path, include
from cards.api.views import CreditCardViewSet

router = DefaultRouter()
router.register('cards', CreditCardViewSet, basename="cards")

urlpatterns = [
    path('', include(router.urls)),
]
