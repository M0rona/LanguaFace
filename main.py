from translate import Translator

translator = Translator()

example = "Bom dia pessoal, é um prazer estar aqui com vocês"
example_translated = translator.translate(example, "en")
print(example_translated)