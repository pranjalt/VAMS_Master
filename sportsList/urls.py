from django.conf.urls import include, url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'PlayerSportListWS', views.PlayerListViewSet, 'sports_id')
router.register(r'CoachRegisterWS',views.CoachRegistration)
router.register(r'SportListWS', views.SportListViewSet)
router.register(r'CoachListWS',views.CoachList,'coach_id')
router.register(r'PlayerListWS',views.PlayerList,'player_id')
router.register(r'PlayerLoginWS',views.PlayerLogin,{'user_name','password'})
router.register(r'CoachLoginWS',views.CoachLogin,{'user_name','password'})
router.register(r'PlayerRegisterWS', views.PlayerRegistration)
router.register(r'CountryWS', views.Country)
router.register(r'ProvinceWS', views.Province)
router.register(r'RoleWS', views.Role)
router.register(r'CityWS', views.City)
router.register(r'GenderWS', views.Gender)
router.register(r'SecurityQuestionsWS', views.SecurityQuestions)
router.register(r'SportsWS', views.Sports)

urlpatterns = [
    
    url(r'^login_form/', views.login_form),
    url(r'^login/',views.login),
    url(r'^provience_home/', views.provience_home, name="prv_home"),
    #url(r'^registration/', views.registration),
    url(r'^players_list/', views.players_list),
    url(r'^sports_list/', views.sports_list),
    url(r'^registration_form/', views.registration_form),
    url(r'^logout/$', views.logout_page),
    url(r'^sport_list/$', views.sport_list),
    url(r'^hello/$', views.Country),
    url(r'^submit_registration_form/$', views.registration),
    url(r'^', include(router.urls)),
	#url(r'^CoachRegisterWS/',views.CoachRegistration.as_view()),
   
    url(r'^rest-auth/', include('rest_auth.urls'))
    
]

