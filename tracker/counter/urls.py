from rest_framework import routers
from django.urls import path, include
from .views import NumberViewSet

router = routers.DefaultRouter()
router.register(r'counter', NumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]