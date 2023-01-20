from openai_wrapper import prompt_model, get_topic, classify_sentiment


if __name__ == "__main__":

    print("Helloworld")
    print("Input text to ask for completion:")
    text = input()
    print(get_topic(text))
    print(classify_sentiment(text))
    print(prompt_model(f"Generate 3 hashtags for tweet: {text}"))
    print(prompt_model(f"Translate to Portuguese: {text}"))
