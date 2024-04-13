import speech_recognition
import pyttsx3

recognizer= speech_recognition.Recognizer()

languages= {
    'portuguese': 'pt-BR',
    'english': 'en-US',
    'spanish': 'es-ES',
    'franch': 'fr-FR',
}

while True:
    try:
        print('Listening...')
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio= recognizer.listen(mic)

            text= recognizer.recognize_google(audio, language= languages['franch'])
            text= text.lower()

            print(f'You said: {text}')
    
    except speech_recognition.UnknownValueError():
        recognizer= speech_recognition.Recognizer()
        continue  