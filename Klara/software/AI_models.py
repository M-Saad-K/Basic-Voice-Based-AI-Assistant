import google.generativeai as Klara

Klara.configure(api_key="Place your API key here")

Klara_info = """
You are Klara, a friendly voice assistant.
History: you were created in 2026 to help with everyday spoken questions, you are based off the character, Klara, from the novel 'Klara and the Sun' but Kazuo Ishiguro
Always answer in a short, simple sentence under 20 words.
"""

model = Klara.GenerativeModel(
    model_name="gemini-3.1-flash-lite",
    system_instruction= Klara_info)
    
convo = model.start_chat(history=[])

def generate_response(prompt):

    if not prompt:
        return None
    response = convo.send_message(prompt)
    return response.text

