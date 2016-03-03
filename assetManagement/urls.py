from django.conf.urls import include, url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'^sportsByVendorWS',views.get_sports_by_vendor_ws,{'vendor_id'})
router.register(r'^assetsBySportWS',views.get_assets_by_vendorSports_ws,{'vendor_id','sports_id'})
router.register(r'^createAssetMgmtWS',views.create_asset_management_ws)
urlpatterns = [
    url(r'^vendorsWS/$',views.get_vendor_list_ws.as_view()),
    url(r'^assetDistributionListWS/$',views.assets_distribution_list_ws.as_view()),
    url(r'^schoolListWS/$',views.school_list_ws.as_view()),
    url(r'^', include(router.urls)),
]