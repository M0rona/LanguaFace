import cv2
import numpy as np
from PIL import Image

def showErrorVideo():
    error_image = Image.open('./images/error-message.jpg')
    frameArray = np.array(error_image)
    frame_error = cv2.cvtColor(frameArray, cv2.COLOR_RGB2BGR)

    while True:
        cv2.imshow('Erro', frame_error)
        
        if cv2.waitKey(1) == 27 or cv2.getWindowProperty('Erro', cv2.WND_PROP_VISIBLE) < 1:
            break

    