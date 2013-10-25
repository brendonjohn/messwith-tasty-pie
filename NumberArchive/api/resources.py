__author__ = 'brendonjohn'
from tastypie.resources import ModelResource
from NumberArchive.models import MagicNumber
from tastypie import fields
from num2words import num2words

class MagicNumberResource(ModelResource):
    number_to_word = fields.CharField()

    class Meta:
        queryset = MagicNumber.objects.all()
        allowed_methods = ['get']

    def hydrate_number(self, bundle):
        return int(bundle.data['number']) * 2

    def dehydrate_number_to_word(self, bundle):
        return num2words(bundle.data['number'])

    def dehydrate(self, bundle):
        bundle.data['test_field'] = "Hello, Tasty"
        return bundle