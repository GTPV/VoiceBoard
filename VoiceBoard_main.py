import VoiceBoard_functions as vf

def main():
    while(True):
        #VoiceInput = vf.audioInput()
        VoiceInput = input()
        VoiceInputList = VoiceInput.split()
        VoiceInputListLower = []
        for i in range(len(VoiceInputList)):
            VoiceInputListLower.append(VoiceInputList[i].lower())
        VoiceKeyword = VoiceInputListLower[0]




        if(VoiceKeyword == 'endblock'):

            break





        elif(VoiceKeyword == "breakline"):

            vf.typeInput("\n")





        elif(VoiceKeyword == "print"):

            StringToPrint = vf.CaseController.MergeAddSpace(VoiceInputList[1:])
            vf.typePrint(StringToPrint)





        elif(VoiceKeyword == "define"):

            if(VoiceInputListLower[1] == "variable"):
                variableType = VoiceInputList[2]
                variableCase = VoiceInputList[3]
                if "initialize" in VoiceInputListLower:
                    InitializerIndex = VoiceInputListLower.index("initialize")
                    variableName = VoiceInputList[4:InitializerIndex]
                    initialValue = VoiceInputList[InitializerIndex+1:]
                    vf.defineVariable(variableType, variableCase, variableName, initialValue) 
                else:
                    variableName = VoiceInputList[4:]
                    vf.defineVariable(variableType, variableCase, variableName)





        elif(VoiceKeyword == "for"):

            if(VoiceInputListLower[1] == "times"):
                reps = VoiceInputList[2]
                vf.typeRepsFor(reps)
                main()
                vf.closeCurlyBracket()
            else:
                ConditionIndexes = {'initial' : 0, 'terminal' : 0, 'change' : 0}
                for i in ConditionIndexes.keys():
                    if i in VoiceInputListLower:
                        ConditionIndexes[i] = VoiceInputListLower.index(i)
                vf.typeClassicFor(VoiceInputList[ConditionIndexes['initial']+1:ConditionIndexes['terminal']], VoiceInputList[ConditionIndexes['terminal']+1:ConditionIndexes['change']], VoiceInputList[ConditionIndexes['change']+1:])
                main()
                vf.closeCurlyBracket()





        elif(VoiceKeyword == "if"):

            if(len(VoiceInputList) == 1):
                vf.typeIf()
                main()
                vf.closeCurlyBracket()





        elif(VoiceKeyword == 'else'):

            vf.typeElse()
            main()
            vf.closeCurlyBracket()




main()
