import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def prompt_model(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # check response json object
    # print(json.dumps(response, indent=4))
    text = response["choices"][0]["text"]
    for x in ["\n", "\r"]:
        text = text.replace(x, "")
    return text


def classify_sentiment(tweet: str):
    return prompt_model(f"Classify the sentiment of tweet: {tweet}")


def get_topic(tweet: str):
    return prompt_model(f"Return topic of tweet: {tweet}")


if __name__ == "__main__":

    text_0 = "What a productive day I'm having!"
    text_1 = "This sucks. I'm bored 😠"
    text_2 = "ChatGPT is a model of OpenAI library trained on NLP and code."

    print("-----")
    print("-----")
    print(text_0)
    print(get_topic(text_0))
    print(classify_sentiment(text_0))
    print(prompt_model(f"Generate 3 hashtags for tweet: {text_0}"))
    print(prompt_model(f"Translate to Portuguese: {text_0}"))
    print("-----")
    print(text_1)
    print(get_topic(text_1))
    print(classify_sentiment(text_1))
    print(prompt_model(f"Generate 3 hashtags for tweet: {text_1}"))
    print(prompt_model(f"Translate to Portuguese: {text_1}"))
    print("-----")
    print(text_2)
    print(get_topic(text_2))
    print(classify_sentiment(text_2))
    print(prompt_model(f"Generate 3 hashtags for tweet: {text_2}"))
    print(prompt_model(f"Translate to Portuguese: {text_2}"))
    print("-----")
    print("-----")
