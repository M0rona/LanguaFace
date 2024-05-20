import cv2 
import threading
import textwrap
import win32com.client
import pyvirtualcam
from PIL import ImageFont, ImageDraw, Image
import numpy as np

from speech import voice

recognized_text = ""

def listar_nomes_dispositivos_video_windows():
    wmi = win32com.client.GetObject("winmgmts:")
    cameras = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE PNPClass='Camera'")
    nomes_dispositivos = [camera.Name for camera in cameras]
    return nomes_dispositivos

def encontrar_indice_por_nome(nomes_dispositivos):
    for index in range(len(nomes_dispositivos)):
        if nomes_dispositivos[index]:
            return index
    return -1

#TESTE  
dict_index_names = {}
nomes= listar_nomes_dispositivos_video_windows()
indice = encontrar_indice_por_nome(nomes)
dict_index_names.update({indice: nomes})
print(dict_index_names)

def startCaptureVideo(langIn, langOut, deviceIndex):
    def recognize_speech():
        global recognized_text
        while True:
            recognized_text = voice(langIn, langOut)
    
    def capture_video():
        # Crie a janela
        cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

        # Faça a janela aparecer em cima de todas as outras
        cv2.setWindowProperty('Video', cv2.WND_PROP_TOPMOST, 1)

        vid = cv2.VideoCapture(deviceIndex) 
        font = langOut == 'zh-cn' and ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 35) or ImageFont.truetype("C:\WINDOWS\Fonts\ARIAL.TTF", 35)
        color = "yellow"
        thickness = 2

        with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:
            while True: 
                ret, frame = vid.read() 

                # Obtenha a largura do quadro
                frame_width = frame.shape[1]

                # Calcule a largura da caixa de texto
                text_width = font.font.getsize(recognized_text)[0][0]

                # Se a largura do texto for maior que a largura do quadro, quebre o texto
                if text_width > frame_width:
                    wrapped_text = textwrap.wrap(recognized_text, width=int(frame_width / (thickness * 9)))
                else:
                    wrapped_text = [recognized_text]

                # Posição y 
                y = 400 - ((len(wrapped_text) - 1) * 40)

                #Transformando o frame em imagem
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(image)

                # Itere sobre as linhas do texto quebrado
                for line in wrapped_text:
                    # Calcule a posição x para centralizar o texto
                    text_width = font.font.getsize(line)[0][0]
                    x = int((frame_width - text_width) / 2)
                    
                    # Coloque o texto no frame linha a linha
                    draw = ImageDraw.Draw(pil_image)
                    draw.text((x, y), line, fill=color, font=font)

                    # Atualize a posição y para a próxima linha
                    y += 40

                # Converte a imagem de volta para o frame
                pilImage = np.asarray(pil_image)
                frame_bgr  = cv2.cvtColor(pilImage, cv2.COLOR_RGB2BGR) 

                # Envia o frame para a câmera virtual
                cam.send(frame_bgr)

                cam.sleep_until_next_frame()

                # Exibe o frame no preview
                cv2.imshow('Video', frame_bgr)
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break

        vid.release() 
        cv2.destroyAllWindows()

    # Cria e inicia as threads para rodar as duas funções ao mesmo tempo
    speech_thread = threading.Thread(target=recognize_speech)
    video_thread = threading.Thread(target=capture_video)
    speech_thread.start()
    video_thread.start()