__author__ = 'hari'

from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items',views.ItemsViewSet)


urlpatterns = patterns(
    '',
    url(r'^',
        include(router.urls)),
)