from googletrans import Translator

translate = Translator()
def translator(entry, combo):
    texto = entry.get()
    comboText = combo.get()
    
    comboItems = {
        "Inglês": "en",
        "Português": "pt",
        "Espanhol": "es",
        "Francês": "fr",
    }
        
    return translate.translate(texto, dest=comboItems[comboText]).text