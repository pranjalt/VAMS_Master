from django.db import models
from cms.models import CMSPlugin
from registerApp.models import Register


class AppPLugin(CMSPlugin):
    register = models.ForeignKey(Register)

    def __unicode__(self):
        return self.register.name