import googletrans

tradutor = googletrans.Translator()

def traduzir(entry, combo):
    texto = entry.get();
    
    traducao = tradutor.translate(texto, 'en')
    
    return traducao.text
