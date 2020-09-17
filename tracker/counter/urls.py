from rest_framework import routers
from django.urls import path, include
from .views import NumberViewSet, TemViewSet

router = routers.DefaultRouter()
router.register(r'counter', NumberViewSet)
router.register(r'temtem', TemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]