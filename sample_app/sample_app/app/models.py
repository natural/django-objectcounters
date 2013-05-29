from django.db import models

from django.contrib.sites.models import Site


class MySite(models.Model):
    """
    Really dumb model for admin testing purposes
    """
    site = models.ForeignKey(Site)

    def __unicode__(self):
        return unicode(self.site)
