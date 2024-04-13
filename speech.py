import speech_recognition
import pyttsx3

recognizer= speech_recognition.Recognizer()

def voice(combo):
    comboAudio = combo.get()
    languages= {
        "Inglês": "en",
        "Francês": "fr",
        "Espanhol": "es",
        "Português": "pt",
    }
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio= recognizer.listen(mic)
                text= recognizer.recognize_google(audio, language= languages[comboAudio]).lower()  
                return text

        except speech_recognition.UnknownValueError:
            recognizer= speech_recognition.Recognizer()
            print("Sorry, i didn't catch that. Please, try again.")
            continue
        
# while True:
#     try:
#         print('Listening...')
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             audio= recognizer.listen(mic)

#             text= recognizer.recognize_google(audio, language= languages['Inglês']).lower()
#             print(f'You said: {text}')
    
#     except speech_recognition.UnknownValueError:
#         recognizer= speech_recognition.Recognizer()
#         print("Sorry, i didn't catch that. Please, try again.")
#         continue  