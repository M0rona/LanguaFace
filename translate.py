import googletrans

translator = googletrans.Translator()

# print(googletrans.LANGUAGES)

text_1 = "Bom dia, é um prazer estar aqui com vocês"
translated = translator.translate(text_1, "en")
print(translated.text)

text_2 = "Hello guys, this tool is really interesting, right?"
translated_2 = translator.translate(text_2, "pt")
print(translated_2.text)