from django.contrib import admin

from .models import Carousel_video_video

class CarosuelAdmin(admin.ModelAdmin):
  model=Carousel_video_video
  exclude =('cmsplugin_ptr',)
    

admin.site.register(Carousel_video_video, CarosuelAdmin)


