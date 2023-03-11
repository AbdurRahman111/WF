from rest_framework import serializers
from datetime import datetime

from .models import Team_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class Team_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Team_Model
        fields="__all__"


