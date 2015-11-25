__author__ = 'hari'
from django.conf.urls import patterns, url, include
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'info',views.UserInfoViewSet,base_name='Address')

urlpatterns = patterns(
    '',

    #for Address
    url(r'^' , include(router.urls)),
    #Login with Facebook
    url(r'^register-by-token/(?P<backend>[^/]+)/$',
        views.register_by_access_token,name='register')
)