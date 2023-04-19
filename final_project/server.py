from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text=language_translator.translate(textToTranslate, model_id='en-fr').get_result()
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text=language_translator.translate(textToTranslate, model_id='fr-en').get_result()
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render 
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
