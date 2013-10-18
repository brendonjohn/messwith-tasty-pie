from django.db import models


class MagicNumber(models.Model):
    title = models.CharField("Title", max_length=20)
    number = models.IntegerField()

    def __unicode__(self):
        return self.title