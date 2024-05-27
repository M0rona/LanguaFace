import customtkinter as tk
from PIL import Image
from webcam import startCaptureVideo
from devices import listDevices

window = tk.CTk()
devicesVideo = listDevices('video')
devicesAudio = listDevices('audio')

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
        "Português": "pt-br",
        "Mandarim": "zh",
    }

    startCaptureVideo(
        languages[comboInput.get()], 
        languages[comboOutput.get()], 
        devicesVideo.index(comboDevicesVideo.get()),
        devicesAudio.index(comboDevicesAudio.get())
    )
    window.destroy()    

labelDevicesVideo = tk.CTkLabel(window, text="Entradas de vídeo")
labelDevicesVideo.grid(row=2, column=0, columnspan=2, pady=10)

comboDevicesVideo = tk.CTkComboBox(window, values=devicesVideo)
comboDevicesVideo.grid(row=3, column=0, columnspan=2)

labelDevicesAudio = tk.CTkLabel(window, text="Entradas de áudio")
labelDevicesAudio.grid(row=2, column=1, columnspan=2, pady=10)

comboDevicesAudio = tk.CTkComboBox(window, values=devicesAudio)
comboDevicesAudio.grid(row=3, column=1, columnspan=2)

buttonStart = tk.CTkButton(window, text="Iniciar", command=clickStart)
buttonStart.grid(row=4, column=1, columnspan=1, pady=30)

window.mainloop()