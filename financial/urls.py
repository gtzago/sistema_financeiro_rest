from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from . import views


router = routers.DefaultRouter()
router.register(r'financial-accounts', views.FinancialAccountViewSet)
router.register(r'transactions', views.TransactionViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]