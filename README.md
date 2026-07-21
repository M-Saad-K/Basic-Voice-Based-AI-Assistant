# Based Voice Based AI Assistant:
## Overall Description:
Made this simple user speech input and audio output AI assistant, similar to an Alexa, called 'Klara'.
I used Python for programming this project, and Gemini-3.1-flash-lite as the model that answers your speech questions with short 2O word speech sentences.
Klara uses the Gemini API, Vosk Speech Model, and TTS.api.

## Operation Description:
It takes the userinput from your voice through speech_to_text.py, which is handled by the vosk-model-small-en-us-0.15 through the listen_with_vosk() function.
The text input is then fed into the generate_response() function in AI_models.py, which uses the Gemini-3.1-flash-lite model and generates a response that is less than 20 words long.
That text response is then passed into play_text() function in imp_text_to_speech.py, which uses TTS.api to make a output.wav file that is then played from your speaker.
To run this program, because of pyaudio, you have to install and use Python.2.7 using Deadsnakes.
You also need the Vosk model and a Gemini API key
