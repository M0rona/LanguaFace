import customtkinter as tk
from translate import translator
from speech import voice
from PIL import Image


window = tk.CTk()

#Definiçao da tela
window.geometry("700x500")
window.resizable(False, False)
window.title("LanguaFace")

title = tk.CTkLabel(window, text="O que deseja traduzir?")
title.pack(padx=10, pady=10)

#input box texto traduçao
text = tk.CTkEntry(window, placeholder_text="Digite aqui...", width=500)
text.pack(padx=10)

#botao voz
def clickVoice():
    print(voice(text, combo))
    
my_image = tk.CTkImage(light_image=Image.open("./images/microfone.png"), dark_image=Image.open("./images/microfone.png"), size=(35, 35))
buttonVoice = tk.CTkButton(window, image=my_image, width=30, height=30, text= "", command=clickVoice)
buttonVoice.pack(padx=25, pady=25)


#box linguagens
labelLanguages = tk.CTkLabel(window, text="Informe o idioma")
labelLanguages.pack(padx=10, pady=8)

combo = tk.CTkComboBox(window, values=["Inglês", "Português", "Espanhol", "Francês", "Mandarim"])
combo.pack(padx=10)

#box frase traduzida
traducao = tk.CTkLabel(window, width=500, bg_color="#242424", text="Tradução", corner_radius=10, fg_color="#343638")
traducao.pack(padx=10, pady=20)

def click():
    traducao.configure(text=translator(text, combo))

button = tk.CTkButton(window, text="Traduzir", command=click)
button.pack(padx=10, pady=30)

window.mainloop()