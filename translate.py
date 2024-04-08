import googletrans

tradutor = googletrans.Translator()

def traduzir(entry, combo):
    texto = entry.get()
    combo = combo.current();
    
    traducao = tradutor.translate(texto, 'en')
    
    return traducao.text
