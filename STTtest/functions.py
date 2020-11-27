import speech_recognition as sr


r = sr.Recognizer()
print("r = sr.Recognizer()")

mic = sr.Microphone()
print("Mic = sr.Microphone()")




with mic as source:
    print("with mic as source")
    #r.adjust_for_ambient_noise(source, 1)
    #print("r.adjust_for_ambient_noise(source, 1)")
    print("mic input...")
    audio = r.listen(source, timeout = 3)
    print("audio = r.listen(source, timeout = 3)")
    print("Stop talking")
    try:
        text = r.recognize_google(audio)
        print("text = r.recognize_google(audio)")
        print(text)
    except:
        print("Can't recognize any voice")
print("Program is over")
