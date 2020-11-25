import os
import pandas as pd
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =r"D:\Python\my-translation-api-7f9d257e6b35.json"

translate_client = translate.Client()

languages=translate_client.get_languages()

languagelist = pd.DataFrame(languages)

print(languagelist)

text = open('input.txt', 'r', encoding="utf8").read()

target = 'uk'

result = translate_client.translate(
    text,
    target_language=target
)

print(u"Text: {}".format(result["input"]))
print(u"Translation: {}".format(result["translatedText"]))
print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


