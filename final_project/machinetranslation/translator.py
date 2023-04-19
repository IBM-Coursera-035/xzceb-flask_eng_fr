import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create language translator instance:

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
language_translator.set_service_url(url)

# Function to translate English to French:

def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text=englishText,
        model_id='en-fr'

    ).get_result()

    return frenchText.get("translations")[0].get("translation")

# Function to translate French to English:

def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
        text=frenchText,
        model_id='en-fr'

    ).get_result()

    return englishText.get("translations")[0].get("translation")    

