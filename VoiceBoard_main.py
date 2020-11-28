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
    elif(VoiceKeyword == "define"):
        if(VoiceInputList[1] == "variable"):
            variableType = VoiceInputList[2]
            variableCase = VoiceInputList[3]
            if "initialize" in VoiceInputList:
                InitializerIndex = VoiceInputList.index("initialize")
                variableName = VoiceInputList[4:InitializerIndex]
                initialValue = VoiceInputList[InitializerIndex+1]
                vf.defineVariable(variableType, variableCase, variableName, initialValue) 
            else:
                variableName = VoiceInputList[4:]
                vf.defineVariable(variableType, variableCase, variableName)
