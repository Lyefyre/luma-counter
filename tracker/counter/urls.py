from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from .views import NumberViewSet

router = routers.DefaultRouter()
router.register(r'counter', NumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^counter/(?P<pk>[0-9,a-z,-]+)/$', NumberViewSet)
]

urlpatterns += router.urls