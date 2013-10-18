__author__ = 'brendonjohn'
from tastypie.resources import ModelResource
from NumberArchive.models import MagicNumber


class MagicNumberResource(ModelResource):
    class Meta:
        queryset = MagicNumber.objects.all()
        allowed_methods = ['get']