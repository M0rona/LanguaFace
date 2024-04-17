import customtkinter as tk
from translate import translator
from speech import voice
from PIL import Image


window = tk.CTk()

#Definiçao da tela
window.geometry("500x500")
window.resizable(False, False)
window.title("LanguaFace")

# Configura as colunas para terem a mesma largura
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#box linguagens de entrada
labelInput = tk.CTkLabel(window, text="Idioma de entrada")
labelInput.grid(row=0, column=0, columnspan=1)

comboInput = tk.CTkComboBox(window, values=["Inglês", "Português", "Espanhol", "Francês", "Mandarim"])
comboInput.grid(row=1, column=0, columnspan=1)

# Icone central
icon = tk.CTkImage(light_image=Image.open("./images/ArrowDark.png"), dark_image=Image.open("./images/ArrowWhite.png"), size=(34, 34))

icon_label = tk.CTkLabel(window, image=icon, text="")
icon_label.image = icon  # Guarda uma referência à imagem para evitar que ela seja coletada como lixo
icon_label.grid(row=1, column=1, columnspan=1)

# box linguagens de saida
labelOutput = tk.CTkLabel(window, text="Idioma de saida")
labelOutput.grid(row=0, column=2, columnspan=1)

comboOutput = tk.CTkComboBox(window, values=["Inglês", "Português", "Espanhol", "Francês", "Mandarim"])
comboOutput.grid(row=1, column=2, columnspan=1)

window.mainloop()