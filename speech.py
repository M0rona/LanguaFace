import speech_recognition
import pyttsx3
from translate import translator

recognizer= speech_recognition.Recognizer()

#voice function using speech recognition
def voice(langIn, langOut, micIndex):
    recognizer= speech_recognition.Recognizer()
    
    while True:
        try:
            print('Listening...')
            with speech_recognition.Microphone(device_index=micIndex) as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio= recognizer.listen(mic)
                text= recognizer.recognize_google(audio, language=langIn) 
                return translator(text.lower(), langOut)


        except speech_recognition.UnknownValueError:
            recognizer= speech_recognition.Recognizer()
            print("Não entendi, tente novamente.")
            continue