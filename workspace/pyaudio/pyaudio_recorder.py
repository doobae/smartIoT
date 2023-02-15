import pyaudio
import wave
CHUNK = 1024 # 버퍼 크기
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000 # 44100
RECORD_SECONDS = 5 # 녹음시간 5초
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()
stream = p.open(input_device_index = 1, # 자신에게 맞는 장치 번호 지정, 생략가능
         format=FORMAT,
         channels=CHANNELS,
         rate=RATE,
        input=True,
        frames_per_buffer=CHUNK)