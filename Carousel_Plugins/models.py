from django.db import models
from cms.models import CMSPlugin
from Carousel.models import Carousel_video_video

# Create your models here.
class CarouselPlugins(CMSPlugin):
    video = models.ForeignKey(Carousel_video_video)

   