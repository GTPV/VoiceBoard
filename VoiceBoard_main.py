import VoiceBoard_functions as vf

while(True):
    #VoiceInput = vf.audioInput()
    VoiceInput = input()
    VoiceInputList = VoiceInput.split()

    VoiceKeyword = VoiceInputList[0]

    if(VoiceKeyword == "print"):
        StringToPrint = ""
        for i in range(1, len(VoiceInputList), 1):
            StringToPrint += VoiceInputList[i]
            StringToPrint += " "
        StringToPrint = StringToPrint[:-1]
        vf.typePrint(StringToPrint)
