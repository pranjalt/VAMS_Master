from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from Carousel_Plugins.models import CarouselPlugins
from django.utils.translation import ugettext as _
#from Carousel.views import carousel
from Carousel.models import *

class Carousel_Plugins(CMSPluginBase):
    name = _('video carousel')
    cache = False
    render_template = 'Carousel_Plugins/Carousel_Plugins.html'
 
    def render(self, context, instance, placeholder):
      videos = Carousel_video_video.objects.all()
      for video in videos:
       var=""+str(video.movie_url)     
       var=var.replace("https:","")      	 
       var=var.replace("watch?v=","embed/")
       var=var+"?enablejsapi=1&version=3&playerapiid=ytplayer"       
       video.movie_url=var
      context.update({'instance': instance,'model':CarouselPlugins,'videos':videos})
      return context
		
plugin_pool.register_plugin(Carousel_Plugins)