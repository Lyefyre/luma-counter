from rest_framework import routers
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from .views import NumberViewSet

router = routers.DefaultRouter()
router.register(r'counter', NumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^counter/(?P<pk>[0-9,a-z,-]+)/$', NumberViewSet),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]

urlpatterns += router.urls