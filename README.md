# Based Voice Based AI Assistant - Klara
## Overall Description:
Made this simple user speech input and audio output AI assistant, similar to an Alexa, called 'Klara'.
I used Python for programming this project, and Gemini-3.1-flash-lite as the model that answers your speech questions with short 20 word speech sentences.
Klara uses the Gemini API, Vosk Speech Model, and TTS.api.

## Operation Description:
1. It takes the userinput from your voice through speech_to_text.py, which is handled by the vosk-model-small-en-us-0.15 through the listen_with_vosk() function.
  
2. The text input is then fed into the generate_response() function in AI_models.py, which uses the Gemini-3.1-flash-lite model and generates a response that is less than 20 words long. Klara, in AI_models.py, is also given a brief overview of themselves (including name and response expression) before it answers any prompt.

3. That text response is then passed into play_text() function in imp_text_to_speech.py, which uses TTS.api to make a output.wav file that is then played from your speaker.

*The operation is handled by the AI_speech_integretion.py file*

## Set Up Instructions:
### Step 1: Install the Files
Please git clone the code files and folders from the Github repo by using:
```
git clone https://github.com/M-Saad-K/Basic-Voice-Based-AI-Assistant.git
```
### Step 2: Install Vosk Model:
The vosk model is used for speech to text recognition. Please delete the empty vosk folder inside ```packages``` and install the Vosk model from [The Alphacephei Website](https://alphacephei.com/vosk/models)

### Step 3 : Install packages using Pip and Python Environment:
Several packages are required fro the project, including...
```
cvzone
pyserial
vosk
SpeechRecognition
google.generativeai
sounddevice
TTS
pydub
ffmpeg
```
These packages are included in ```req.txt```.
- Create a Python Environment using Python 3.10 using
  ```
  python3.10 -m venv venv
  ```
- Use Pip to Install Requirements
  ```
  pip install -r req.txt
  ```
### Step 4 : Create a Gemini API Key:
Go to the [Gemini API Website](https://ai.google.dev/gemini-api/docs/api-key?authuser=1) and create a Gemini Key for the Gemini 3.1 Lite Model.
Then paste your key into ```AI_models.py```, where it states ```"Place your API key here"```

## How to Run:
- Go into Terminal (VS code)
- To activate the venv do this:
```source venv/bin/activate```
- Then go to the software folder (Linux):
```cd software```
- Then run the ```AI_speech_integretion.py``` file:
```python AI_speech_integretion.py```
- It will then set up itself in Terminal, this will take 2 minutes.
- Then when it prints "Listening" in Terminal, you then speak.
- To turn it off, type ```Ctrl + C``` in Terminal
