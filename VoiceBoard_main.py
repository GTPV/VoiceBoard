import VoiceBoard_functions.py

while(True):
    VoiceInput = audioInput()
    VoiceInputList = VoiceInput.split()

    VoiceKeyword = VoiceInputList[0]

    if(VoiceKeyword == "print"):
        StringToPrint = ""
        for i in range(1, VoiceInputList.len(), 1):
            StringToPrint += VoiceInputList[i]
            StringToPrint += " "
        StringToPrint -= " "
        typePrint(StringToPrint)
