"""
@ Author: Muhammad Saad Khan
@ Date: 04-06-2026
@ Title: AI Speech Integration for Klara
@ Description: This module integrates speech recognition and text-to-speech capabilities into Klara,
"""
from speech_to_text import listen_with_vosk
from imp_text_to_speech import play_text
from AI_models import generate_response

## Take it in the user's voice at text
## Send that voice to the AI model and get a response
## Convert that response to speech and play it back to the user
## Repeat in a loop

def main():
    while True:
        user_input = listen_with_vosk()
        print("User said:", type(user_input))
        if user_input:
            print("User said:", user_input)
            response = generate_response(user_input)
            print("Strathbot:", type(response))

            play_text(response)
        else:
            play_text("Sorry, missed that")

main()