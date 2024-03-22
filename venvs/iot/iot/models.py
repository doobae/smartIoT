from django.db import models


class Sensor(models.Model):
  place = models.CharField(max_length=50)     # 설치 장소
  category = models.CharField(max_length=50)  # 센서 종류
  value = models.FloatField()                 # 센서 값
  created_at = models.DateTimeField()         # 측정 날짜-시간
