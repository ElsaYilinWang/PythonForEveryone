# CS6361 Final Project

# Problem 2:
# You have five texts, each a different language.
# You want to be able to detect the language for each of the texts.
# You want to be able to repeat that on other texts of the same languages.

# Reference
# Fadheli, A. (n.d.). How to Translate Languages in Python - Python Code. [online] thepythoncode.com.
# Available at: https://thepythoncode.com/article/translate-text-in-python?utm_content=cmp-true [Accessed 2 Nov. 2023].

# import python library googletrans
import googletrans
import random

# create an object from googletrans class
translator = googletrans.Translator()

languages = []

# choose a random piece of English text
English_text = "Whether you're travelling to the islands or the mountains of Thailand, you're likely to spend at least one night in " \
               "its capital city on the way. Bangkok might be noisy and polluted but it's also an exciting city with plenty of " \
               "things to see and do. Why not make it a longer stay?"

languages.append(English_text)


# create a function to translate English to other languages
def text_translate(original_text, desired_language):

    translation = translator.translate(text=original_text, dest=desired_language)
    return translation.text


# translate English to Spanish
Spanish_text = text_translate(English_text, 'es')
languages.append(Spanish_text)

# translate English to German
German_text = text_translate(English_text, 'de')
languages.append(German_text)

# translate English to Arabic
Arabic_text = text_translate(English_text, 'ar')
languages.append(Arabic_text)

# translate English to French
French_text = text_translate(English_text, 'fr')
languages.append(French_text)


# detect languages using the LANGUAGES dictionary in googletrans
def detect_language(lang_text):
    detection = translator.detect(lang_text)

    print("\nLanguage code:", detection.lang)
    print("\nLanguage:", googletrans.LANGUAGES[detection.lang])

# choose a random piece of text
#text_to_detect = random.choice(languages)
#print(text_to_detect)

# call detect_language function
#detect_language(text_to_detect)

########### Scale Up! ##########

text_entry = input("Please input the text you want to detect:\n")

# To improve the efficiency, only check a slice of string for detection
if len(text_entry) > 15:
    lang_text = text_entry[:16]
    detect_language(lang_text)

else:
    detect_language(text_entry)

