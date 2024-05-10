import cv2 
import threading
import textwrap
import pyvirtualcam
from PIL import ImageFont, ImageDraw, Image
import numpy as np

from speech import voice

recognized_text = ""

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
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = "yellow"
        thickness = 2

        with pyvirtualcam.Camera(width=640, height=480, fps=30) as cam:
            while True: 
                ret, frame = vid.read() 

                # Obtenha a largura do quadro
                frame_width = frame.shape[1]

                # Calcule a largura da caixa de texto
                text_width = cv2.getTextSize(recognized_text, font, font_scale, thickness)[0][0]

                # Se a largura do texto for maior que a largura do quadro, quebre o texto
                if text_width > frame_width:
                    wrapped_text = textwrap.wrap(recognized_text, width=int(frame_width / (thickness * 9)))
                else:
                    wrapped_text = [recognized_text]

                # Posição y 
                y = 400 - ((len(wrapped_text) - 1) * 40)

                # Itere sobre as linhas do texto quebrado
                for line in wrapped_text:
                    # Calcule a posição x para centralizar o texto
                    text_width = cv2.getTextSize(line, font, font_scale, thickness)[0][0]
                    x = int((frame_width - text_width) / 2)

                    #Transformando o frame em imagem
                    image = frame
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    pil_image = Image.fromarray(image)

                    # Setar fontes para o tipo de linguagem:
                    if (langOut == 'zh-cn'):
                        fontText = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 35)
                    else:
                        fontText = ImageFont.truetype("c:\WINDOWS\Fonts\ARIAL.TTF", 35)

                    # Coloque o texto no frame
                    draw = ImageDraw.Draw(pil_image)
                    draw.text((x, y), line, fill=color, font=fontText)

                    image = np.asarray(pil_image)
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)     

                    # Coloque o texto no quadro -- BACKUP ANTIGO
                    #cv2.putText(frame, line, (x, y), font, font_scale, color, thickness)

                    # Atualize a posição y para a próxima linha
                    y += 40

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                cam.send(frame_rgb)

                cam.sleep_until_next_frame()

                cv2.imshow('Video', image)
                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break

        vid.release() 
        cv2.destroyAllWindows()

    # Create and start the threads
    speech_thread = threading.Thread(target=recognize_speech)
    video_thread = threading.Thread(target=capture_video)
    speech_thread.start()
    video_thread.start()