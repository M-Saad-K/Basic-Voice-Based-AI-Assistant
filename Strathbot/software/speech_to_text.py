import vosk
import sounddevice as sd
import json

model = vosk.Model("/home/mr-python/Documents/Summer Plan/Electronic Projects/Basic-Voice-Based-AI-Assistant/Strathbot/packages/vosk-model-small-en-us-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)

def listen_with_vosk():
    q = []

    def callback(indata, frames, time, status):
        q.append(bytes(indata))

    with sd.RawInputStream(samplerate=16000, blocksize=8192, dtype="int16", channels=1, callback=callback):
        print("Listening...")
        while True:
            if not q:
                continue
            data = q.pop(0)
            if len(data) == 0:
                continue
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result).get("text", "")
                print("You said:", text)
                return text
