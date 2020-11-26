import speech_recognition as sr


r = sr.Recognizer()

Mic = sr.Microphone()
print("Mic = sr.Microphone()")




with Mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("mic input...")
    audioInput = r.listen(source, 3)
    print("Stop talking")
    try:
        AudioInput = r.recognize_google(audioInput)
        print(AudioInput)
    except:
        print("Can't recognize any voice")
print("Program is over")
