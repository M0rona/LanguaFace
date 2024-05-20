import customtkinter as tk
from PIL import Image
from webcam import startCaptureVideo, listar_nomes_dispositivos_video_windows, encontrar_indice_por_nome
# from pygrabber.dshow_graph import FilterGraph

window = tk.CTk()
# graph = FilterGraph()

#Definiçao da tela
window.geometry("500x300")
window.resizable(False, False)
window.title("LanguaFace")

# Configura as colunas para terem a mesma largura
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#box linguagens de entrada
labelInput = tk.CTkLabel(window, text="Idioma de entrada")
labelInput.grid(row=0, column=0, columnspan=1, pady=10)

comboInput = tk.CTkComboBox(window, values=["Português", "Inglês" , "Espanhol", "Francês", "Mandarim"])
comboInput.grid(row=1, column=0, columnspan=1)

# Icone central
icon = tk.CTkImage(light_image=Image.open("./images/ArrowDark.png"), dark_image=Image.open("./images/ArrowWhite.png"), size=(34, 34))

icon_label = tk.CTkLabel(window, image=icon, text="")
icon_label.image = icon  # Guarda uma referência à imagem para evitar que ela seja coletada como lixo
icon_label.grid(row=1, column=1, columnspan=1)

# box linguagens de saida
labelOutput = tk.CTkLabel(window, text="Idioma de saida")
labelOutput.grid(row=0, column=2, columnspan=1, pady=10)

comboOutput = tk.CTkComboBox(window, values=["Inglês", "Português", "Espanhol", "Francês", "Mandarim"])
comboOutput.grid(row=1, column=2, columnspan=1)

def clickStart():
    languages = {
        "Inglês": "en",
        "Francês": "fr",
        "Espanhol": "es",
        "Português": "pt",
        "Mandarim": "zh-cn",
    }

    startCaptureVideo(languages[comboInput.get()], languages[comboOutput.get()], 0)
    window.destroy()    

labelDevices = tk.CTkLabel(window, text="Dispositivo de entrada")
labelDevices.grid(row=2, column=1, columnspan=1, pady=10)

comboDevices = tk.CTkComboBox(window, values=listar_nomes_dispositivos_video_windows())
comboDevices.grid(row=3, column=1, columnspan=1)

buttonStart = tk.CTkButton(window, text="Iniciar", command=clickStart)
buttonStart.grid(row=4, column=1, columnspan=1, pady=30)

window.mainloop()