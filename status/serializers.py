from rest_framework import serializers
from .models import *

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','hour','minutes','duration')
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id','status')