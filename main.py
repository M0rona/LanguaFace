import customtkinter as tk
from translate import traduzir

janela = tk.CTk()

janela.geometry("700x500")
janela.resizable(False, False)
janela.title("LanguaFace")

title = tk.CTkLabel(janela, text="Traduza o texto que quiser")
title.pack(padx=10, pady=10)

texto = tk.CTkEntry(janela, placeholder_text="Informe a frase a ser traduzida", width=500)
texto.pack(padx=10)

labelIdioma = tk.CTkLabel(janela, text="Informe o idioma")
labelIdioma.pack(padx=10, pady=10)

combo = tk.CTkComboBox(janela, values=["Inglês", "Português", "Chinês", "Espanhol", "Francês", "Russo"])
combo.pack(padx=10)

def clique():
    traducao = traduzir(texto, combo)
    print(traducao)


botao = tk.CTkButton(janela, text="Traduzir", command=clique)
botao.pack(padx=10, pady=30)

janela.mainloop()