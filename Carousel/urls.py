from django.conf.urls import include, url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'VideoListWS', views.VideoList, {'sports_name','sports_subtype'})
router.register(r'SportSubtypeWS', views.SportSubtype,{'sports_name'})

urlpatterns =  [
    url(r'^', include(router.urls)),
]

