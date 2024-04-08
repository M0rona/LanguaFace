import customtkinter as tk
from translate import traduzir

window = tk.CTk()

window.geometry("700x500")
window.resizable(False, False)
window.title("LanguaFace")

title = tk.CTkLabel(window, text="Traduza o texto que quiser")
title.pack(padx=10, pady=10)

texto = tk.CTkEntry(window, placeholder_text="Informe a frase a ser traduzida", width=500)
texto.pack(padx=10)

labelLanguages = tk.CTkLabel(window, text="Informe o idioma")
labelLanguages.pack(padx=10, pady=10)

combo = tk.CTkComboBox(window, values=["Inglês", "Português", "Chinês", "Espanhol", "Francês", "Russo"])
combo.pack(padx=10)

def click():
    traducao = traduzir(texto, combo)
    print(traducao)


button = tk.CTkButton(window, text="Traduzir", command=clique)
button.pack(padx=10, pady=30)

window.mainloop()