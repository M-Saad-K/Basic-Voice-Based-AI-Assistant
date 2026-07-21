from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play

def play_text(text):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    tts.tts_to_file(text= text)

    sound = AudioSegment.from_file("output.wav", format="wav")
    play(sound)
