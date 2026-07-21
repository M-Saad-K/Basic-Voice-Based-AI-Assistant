import google.generativeai as Klara



def generate_response(prompt):

    Klara.configure(api_key="Your key goes here")

    model = Klara.GenerativeModel(model_name="gemini-3.1-flash-lite")
    #convo = model.start_chat()

    if len(prompt) == 0:
        pass
    else:
        str_list = ["Hi you're Klara, can you answer this question in a short but simple sentence of less then 20 words:", prompt]
        newprompt = " ".join(str_list)
        response = model.generate_content(newprompt)
        return response.text

generate_response("Hi there, how are you. Give me a kind response Strathbot")
