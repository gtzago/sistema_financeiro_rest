from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from . import views


router = routers.DefaultRouter()
router.register(r'financial-accounts', views.FinancialAccountViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
