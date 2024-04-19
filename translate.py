from googletrans import Translator

translate = Translator()
def translator(text, language):        
    return translate.translate(text, dest=language).text