import pyaudio
import wave
#speech to text
text = []

# def listen(self):
audi = pyaudio.PyAudio()
lis = audi.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
print("recording")

for i in range(0, int(44100 / 1024 * 5)):
    data = lis.read(1024)
    text.append(data)
print("finished recording")

# while True:
# 	data = lis.read(1024)
# 	if data in ['close']:
# 		break

# text.append(data)
lis.stop_stream()
lis.close()
audi.terminate()

waveFile = wave.open("sample.wav", 'wb')
waveFile.setnchannels(1)
waveFile.setsampwidth(audi.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(44100)
waveFile.writeframes(' '.join(1024))
waveFile.close()

print(text)