from django.conf.urls import include, url
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'BatchListWS', views.BatchList)
router.register(r'StageListWS', views.StageList)
router.register(r'TrainingRegisterWS', views.TrainingRegister)
router.register(r'TrainingBatchWS', views.TrainingBatch,{'batch_name'})
router.register(r'TrainingPlayerWS', views.TrainingPlayer,{'player_id'})
router.register(r'TrainingCoachWS', views.TrainingCoach,{'coach_id'})

urlpatterns =  [
    url(r'^', include(router.urls)),
]

