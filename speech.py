import speech_recognition
import pyttsx3
from new_translate import translator

#voice function using speech recognition
def voice(langIn, langOut, micIndex):
    recognizer= speech_recognition.Recognizer()
    try:
        print('Listening...')
        with speech_recognition.Microphone(device_index=micIndex) as mic:
            #determina o valor de energia para o reconhecimento de voz
            recognizer.energy_threshold = 8000
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio= recognizer.listen(mic)
            text= recognizer.recognize_google(audio, language=langIn) 
            return translator(text, langIn, langOut)

    except speech_recognition.UnknownValueError:
        #Redefinição para as variaveis nao serem perdidas
        recognizer= speech_recognition.Recognizer()
        recognizer.energy_threshold = 8000
        return "(Não entendi, tente novamente)"