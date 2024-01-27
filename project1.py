#text-speech

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',130)
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
pyttsx3.speak("hello")#we can do it directly
engine.say("welcome to robo speaker by asmit ")
engine.runAndWait()#we can also do text to speech like this
print("4268 to exit ")
while True:
    x=input("write here :-")
    if x=="4268":
        engine.say("bye bye")
        engine.runAndWait()
        break
    else:
        engine.say(x)
        engine.runAndWait()


