# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from rest_framework import routers
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from players import views as playersviews
#from adminlogin import views as loginadmin
from restapp import views
from sportsadmin import views as sportsadmin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^newsfeature/', include('aldryn_newsblog.urls', namespace='newsblog')),
    url(r'^testWS/$', views.Album.as_view()),
    url(r'^playersList/$',playersviews.getPlayersListData),
    url(r'^asset/', include('assetManagement.urls')),
    url(r'^carousel/', include('Carousel.urls')),
    url(r'^sports/', include('sportsList.urls')),
    url(r'^training/', include('Training.urls')),
    #url(r'^adminlogin/', loginadmin.loginadmin),
    url(r'^sportsadmin/', include('sportsadmin.urls')),
    url(r'^listCoach/$',sportsadmin.CoachList),
    url(r'^listAcademy/$',sportsadmin.AcademyList),
    url(r'^listPlayer/$',sportsadmin.PlayerList),
    url(r'^listVideo/$',sportsadmin.VideoList),
    url(r'^listPicture/$',sportsadmin.PictureList,name="listPicture"),
    url(r'^addPlayer/', sportsadmin.addPlayer , name ="addPlayer"),
    url(r'^addVideo/', sportsadmin.addVideo,name ="addVideo"),
    #url(r'^addPhoto/', sportsadmin.addPhoto),
    # vaibhav added
    url(r'^advanceSearch/', sportsadmin.advanceSearch),
    url(r'^loginAdmin/', sportsadmin.sportsAdminLogin),
    url(r'^logoutAdmin/', sportsadmin.adminLogout,name="logout"),
    url(r'^loginAuthentication/', sportsadmin.adminAuthenticate,name="loginSports"),
	# end vaibhav url
    url(r'^sportsadmin/', sportsadmin.addPhoto,name="add"),
    url(r'^deletePlayer/(?:playerId=(?P<playerId>\d+)/)?$', sportsadmin.deletePlayer),
    url(r'^deleteCoach/(?:coachId=(?P<coachId>\d+)/)?$', sportsadmin.deleteCoach),
    url(r'^deleteVideo/(?:videoId=(?P<videoId>\d+)/)?$', sportsadmin.deleteVideo),
    url(r'^deletePhoto/(?:pictureId=(?P<pictureId>\d+)/)?$', sportsadmin.deletePhoto),
    url(r'^deleteAcademy/(?:academyId=(?P<academyId>\d+)/)?$', sportsadmin.deleteAcademy),
    url(r'^viewPlayer/(?:playerId=(?P<playerId>\d+)/)?$',sportsadmin.viewPlayer),
    url(r'^viewCoach/(?:coachId=(?P<coachId>\d+)/)?$',sportsadmin.viewCoach),
    url(r'^viewPhoto/(?:pictureId=(?P<pictureId>\d+)/)?$',sportsadmin.viewPhoto),
    url(r'^viewAcademy/(?:academyId=(?P<academyId>\d+)/)?$',sportsadmin.viewAcademy),
    url(r'^viewVideo/(?:videoId=(?P<videoId>\d+)/)?$',sportsadmin.viewVideo),
    url(r'^addCoach/', sportsadmin.addCoach , name ="addCoach"),
    url(r'^addAcademy/', sportsadmin.addAcademy , name ="addAcademy"),
    url(r'^editAcademy/', sportsadmin.editAcademy , name ="editAcademy"),
	url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
			url(r'', include('django.contrib.staticfiles.urls'))
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
