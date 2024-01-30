from vosk import Model, KaldiRecognizer
import pyaudio
import json

running = True


def start():
    model = Model(r"./vosk-files/vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192, input_device_index=5)
    stream.start_stream()

    while running:
        data = stream.read(4096)

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            result = json.loads(text)
            print(result, type(result))