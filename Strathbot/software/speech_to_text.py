import vosk
import pyaudio
import json
import pygame

pygame.mixer.init()
model = vosk.Model("/home/mr-python/Documents/Summer Plan/Electronic Projects/Strathbot/packages/vosk-model-small-en-us-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)

## No playsound

def listen_with_vosk():
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    print("Listening...")
    ## Here we would play the sound

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            continue
        if recognizer.AcceptWaveform(data):
            ## Playsound here
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            print("You said:", text)
            return text
