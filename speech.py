import speech_recognition
import pyttsx3
from translate import translator

recognizer= speech_recognition.Recognizer()

#voice function using speech recognition
def voice():
    recognizer= speech_recognition.Recognizer()
    # comboAudio = combo.get()
    # languages= {
    #     "Inglês": "en",
    #     "Francês": "fr",
    #     "Espanhol": "es",
    #     "Português": "pt",
    #     "Mandarim": "zh-cn",
    # }
    
    language = "pt"
    
    while True:
        try:
            print('Listening...')
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio= recognizer.listen(mic)
                text= recognizer.recognize_google(audio, language= language) 
                # print(text.lower())
                # return text.lower()
                return translator(text.lower(), "Inglês")


        except speech_recognition.UnknownValueError:
            recognizer= speech_recognition.Recognizer()
            print("Não entendi, tente novamente.")
            continue

# listening voice from pyttsx3 test
# def listen():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say("Hello, how can i help you?")
#     engine.runAndWait()


# languages= {
#         "Inglês": "en",
#         "Francês": "fr",
#         "Espanhol": "es",
#         "Português": "pt",
#         "Mandarin": "zh-cn",
#     }

# while True:
#     try:
#         print('Listening...')
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio= recognizer.listen(mic)

#             text= recognizer.recognize_google(audio, language= languages['Português']).lower()
#             print(f'You said: {text}')
    
#     except speech_recognition.UnknownValueError:
#         recognizer= speech_recognition.Recognizer()
#         print("Sorry, i didn't catch that. Please, try again.")
#         continue  