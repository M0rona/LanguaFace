import googletrans
class Translator():
    def __init__(self):
        self.translator = googletrans.Translator()
        
    def translate(self, text_input, dest_language):
        translated_output = self.translator.translate(text_input, dest_language)
        return translated_output.text