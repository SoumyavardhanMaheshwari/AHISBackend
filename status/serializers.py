from rest_framework import serializers
from .models import *

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','start_datetime','duration','hour', "minute", "second")
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id','status')