import functools
from translate import Translator

# Decorador @lru_cache modificado para trabalhar com argumentos não-hashables
def lru_cache_with_args(func):
    cache = dict()

    @functools.wraps(func)
    def cached_func(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return cached_func

@lru_cache_with_args
def translator(text, langIn, langOut):
    """Traduz um texto para um idioma específico, 
    utilizando cache para otimizar traduções repetidas."""
    trans = Translator(from_lang=langIn, to_lang=langOut)
    translation = trans.translate(text)
    return translation  # Adicionado retorno da tradução