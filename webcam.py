import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import threading
import textwrap
import pytesseract

# Configurando o caminho para o executável do Tesseract '''CASO ELE NÃO ESTEJA NO PATH'''
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


from speech import voice

recognized_text = ""

def startCaptureVideo(langIn, langOut):
    def recognize_speech():
        global recognized_text
        while True:
            recognized_text = voice(langIn, langOut)
  
    def capture_video():
        # Inicie a captura de vídeo
        vid = cv2.VideoCapture(0) 
        font = ImageFont.truetype("arial.ttf", 30)
        color = (0, 255, 255)
        thickness = 2

        while True: 
            ret, frame = vid.read() 

            if ret:
                # Converta o quadro do OpenCV para uma imagem Pillow
                img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(img_pil)

                # Obtenha a largura da imagem
                img_width, img_height = img_pil.size

                # Usa o Tesseract para reconhecer o texto da imagem
                recognized_text = pytesseract.image_to_string(img_pil)

                # Quebre o texto se for muito longo para caber na imagem
                wrapped_text = textwrap.wrap(recognized_text, width=int(img_width / 10))

                # Desenhe o texto na imagem
                y = img_height - (len(wrapped_text) - 1) * 40

                for line in wrapped_text:
                    text_width = draw.textlength(line, font)
                    x = (img_width - text_width) / 2
                    draw.text((x, y), line, fill=(255, 255, 255, 128), font=font)
                    y += 30

                # Converta a imagem Pillow de volta para o formato OpenCV
                frame = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

                # Mostre o quadro com o texto
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'): 
                    break

        vid.release() 
        cv2.destroyAllWindows()

    # Crie e inicie as threads
    speech_thread = threading.Thread(target=recognize_speech)
    video_thread = threading.Thread(target=capture_video)
    speech_thread.start()
    video_thread.start()