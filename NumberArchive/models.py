from django.db import models


class MagicNumber(models.Model):
    title = models.CharField("Title")
    number = models.IntegerField()

    def __unicode__(self):
        return self.title