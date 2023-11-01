import wikipedia
from nltk.tokenize import sent_tokenize

# Function to search Wikipedia and fetch a summary in Hindi
def search_wikipedia(query):
    try:
        wikipedia.set_lang("hi")  # Set the language to Hindi
        result = wikipedia.summary(query)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "माफ़ करें, कुछ संदर्भित जानकारी मिली है, कृपया स्पष्टता देने के लिए और अधिक विस्तृत पृष्ठ का चयन करें।"
    except wikipedia.exceptions.PageError as e:
        return "माफ़ करें, मुझे इस विषय पर कोई जानकारी नहीं मिली।"

# Function to process a user's question and fetch an answer from Wikipedia
def process_question(question):
    # Search Wikipedia for a summary in Hindi
    wikipedia_result = search_wikipedia(question)

    # Split the Wikipedia result into sentences
    sentences = sent_tokenize(wikipedia_result)

    # Return the first sentence as the summarized answer
    if sentences:
        return sentences[0]
    else:
        return "मुझे इस विषय पर कोई जानकारी नहीं मिली।"

# Example usage (for testing)
if __name__ == "__main":
    user_question = "भारत की राजधानी क्या है?"
    bot_response = process_question(user_question)
    print("Bot Response:", bot_response)


# import wikipedia
# from translate import Translator
# from nltk.tokenize import sent_tokenize
# # import openai

# # # OpenAI API key
# # openai.api_key = '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'

# # Function to translate text to Hindi
# def translate_to_hindi(text):
#     translator = Translator(to_lang="hi")
#     translation = translator.translate(text)
#     return translation

# # Function to search Wikipedia and fetch a summary in Hindi
# def search_wikipedia(query):
#     try:
#         wikipedia.set_lang("hi")  # Set the language to Hindi
#         result = wikipedia.summary(query)
#         return result
#     except wikipedia.exceptions.DisambiguationError as e:
#         return "माफ़ करें, कुछ संदर्भित जानकारी मिली है, कृपया स्पष्टता देने के लिए और अधिक विस्तृत पृष्ठ का चयन करें।"
#     except wikipedia.exceptions.PageError as e:
#         return None  # Return None if no information is found on Wikipedia

# # Function to process a user's question and fetch an answer
# def process_question(question):
#     # Translate the user's question to Hindi
#     translated_question = translate_to_hindi(question)

#     # Search Wikipedia for a summary in Hindi
#     wikipedia_result = search_wikipedia(translated_question)

#     # If Wikipedia didn't provide an answer, use ChatGPT API
#     if wikipedia_result is None:
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=f"Translate the following English text to Hindi: '{translated_question}'",
#             max_tokens=100
#         )
#         bot_response = response.choices[0].text.strip()
#     else:
#         bot_response = wikipedia_result

#     # Split the response into sentences
#     sentences = sent_tokenize(bot_response)

#     # Return the first sentence as the summarized answer
#     if sentences:
#         return sentences[0]
#     else:
#         return "मुझे इस विषय पर कोई जानकारी नहीं मिली।"

# # Example usage (for testing)
# if __name__ == "__main__":
#     user_question = "What is the capital of India?"
#     bot_response = process_question(user_question)
#     print("Bot Response:", bot_response)
