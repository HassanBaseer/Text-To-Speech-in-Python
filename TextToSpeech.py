import pyttsx3
while True:
    data = input("Enter text for speech:\n")

    engine = pyttsx3.init()
    engine.say(data)
    engine.runAndWait()
    if data =='exit':
        break