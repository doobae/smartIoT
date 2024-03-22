from rest_framework import serializers
from iot.models import Sensor
class SensorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Sensor
    fields = ('id','place','category', 'value','created_at') # 필드 설정