import functools
from translate import Translator

def lru_cache_with_args(maxsize=128, typed=False):
   
    def decorator(func):
        cache = dict()

        @functools.wraps(func)
        def cached_func(*args, **kwargs):
            if typed:
                key = (func.__name__, *args, tuple(sorted(kwargs.items(), key=lambda item: type(item[1]))))
            else:
                key = args + tuple(kwargs.items())

            if key in cache:
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            return result

        return cached_func

    return decorator

@lru_cache_with_args(maxsize=256, typed=True)  # Ajusta o tamanho do cache conforme necessário
def translator(text, langIn, langOut) :
    """
    Traduz um texto para um idioma específico,
    utilizando cache para otimizar traduções repetidas.
    """
    trans = Translator(from_lang=langIn, to_lang=langOut)
    translation = trans.translate(text)
    return translation
