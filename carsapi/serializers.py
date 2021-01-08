from rest_framework import serializers

from .models import Car, CarRate


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('brandname', 'modelname')


class CarRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarRate
        fields = ('rate', 'carname')
