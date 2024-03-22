import paho.mqtt.client as mqtt
from .models import Sensor
from django.utils import timezone

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+ str(rc))
  if rc == 0:
    print('MQTT 브로커 연결 성공, iot/# 구독 신청')
    client.subscribe("iot/#")  # 연결 성공시 토픽 구독 신청
  else:
    print('연결 실패 :  ', rc)


# 관련 토픽 메시지 수신 콜백 함수      
def on_message(client, userdata, msg):
  value = float(msg.payload.decode())
  print(f" {msg.topic} {value}")
  _, place, category = msg.topic.split('/')
  # DB 저장
  data = Sensor(place=place, category=category, value=value, created_at=timezone.now())
  data.save()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try :
  client.connect("localhost")
  client.loop_start()
except Exception as err:
  print('에러 : %s'%err)
