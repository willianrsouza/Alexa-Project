import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import datetime


class Command:
    def __init__(self, comparar):
        if 'play' in comparar:
            talking.say('I Understand')
            talking.runAndWait()
            talking.say(comparar + 'on Youtube')
            talking.runAndWait()
            pywhatkit.playonyt(comparar)

        elif 'talk about' in comparar:
            talking.say('okay')
            talking.runAndWait()
            talking.say(wikipedia.summary(comparar))

            talking.runAndWait()

        elif 'look for' in comparar:
            talking.say('looking')
            talking.runAndWait()
            pywhatkit.search(comparar)

        elif 'hello' in comparar:
            talking.say('Hello')
            talking.runAndWait()
            talking.say('Why you wish?')
            talking.runAndWait()

        elif 'time' in comparar:
            time = datetime.datetime.now().strftime('%H:%M')
            talking.say('Current time is' + time)
            talking.runAndWait()

        elif 'repeat' in comparar:
            talking.say(comparar)
            talking.runAndWait()

        elif 'news' in comparar:
            pywhatkit.search(comparar)

    pass


talking = pyttsx3.init()
voices = talking.getProperty('voices')
talking.setProperty('rate', 128)
talking.setProperty('voice', voices[1].id)
talking.say('Welcome!')
talking.runAndWait()

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:

            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)
            text_audio = r.recognize_google(audio)

            command = Command(text_audio)
            print('Você disse:  ' + text_audio)
    except:
        talking.say('talk again, please!')
        talking.runAndWait()
