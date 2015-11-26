__author__ = 'hari'
from rest_framework import serializers
from .models import Items

class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Items