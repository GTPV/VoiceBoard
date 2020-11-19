def typePrint():
        print("printf("")")


def defineVariable(variableType, variableName):
        print(variableType, end = "")
        print(" = ", end = "")
        print(variableName)


def typeClassicIf(initialCondition, terminalCondition, changeCondition):
        print("if("+initialCondition+";"+terminalCondition+";"+changeCondition+"){}")
        #moveCursor(-1)


def typeRepsIf(reps):
        print("if(int i = 0; i < "+reps+"; i++){}")
        #moveCursor(-1)

def typeElse():
        print("else{}")
        #moveCursor(-1)
