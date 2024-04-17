from googletrans import Translator

translate = Translator()
def translator(text, language):
    
    comboItems = {
        "Inglês": "en",
        "Português": "pt",
        "Espanhol": "es",
        "Francês": "fr",
        "Mandarim": "zh-cn",
    }
        
    return translate.translate(text, dest=comboItems[language]).text