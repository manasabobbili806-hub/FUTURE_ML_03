import pandas as pd

faq = pd.read_csv("data/faq.csv")

def get_response(message):
    message = message.lower()

    for i in range(len(faq)):
        question = str(faq.iloc[i]["Question"]).lower()
        answer = str(faq.iloc[i]["Answer"])

        if question in message:
            return answer

    return "Sorry, I couldn't understand your question."