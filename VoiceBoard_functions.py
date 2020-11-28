import speech_recognition as sr
#from pynput.keyboard import Key,Controller
#keyboard = Controller()

def audioInput():
    SpeechRecognizer = sr.Recognizer()
    Mic = sr.Microphone()
    with Mic as source:
        AudioInput = SpeechRecognizer.listen(source)
    return SpeechRecognizer.recognize_google(AudioInput)


def typeInput(stringToType):
    #keyboardType(stringToType)
    #print(stringToType)
    textfileType(stringToType)

def textfileType(stringToType):
    testdotcpp = open("testdotcpp.txt", 'a')
    testdotcpp.write(stringToType)
    testdotcpp.close()




def keyboardType(stringToType):
    keyboard.type(stringToType)

def keyboardPress(KeyToPress):
    keyboard.press(KeyToPress)
    #print(KeyToPress)





class CursorController:
        def Left(self, amountToMoveCursor):
            self.Move(amountToMoveCursor, Key.left)
        def Right(self, amountToMoveCursor):
            self.Move(amountToMoveCursor, Key.right)
        def Up(self, amountToMoveCursor):
            self.Move(amountToMoveCursor, Key.up)
        def Down(self, amountToMoveCursor):
            self.Move(amountToMoveCursor, Key.down)
        def Move(self, amountToMoveCursor, KeyToPress):
            for i in range(amountToMoveCursor):
                #keyboardPress(KeyToPress)
                print(KeyToPress)
Cursor = CursorController()



class SpecialSymbol:
    LessThan = "<"
    BiggerThan = ">"
    Plus = "+"
    Times = "×"
    Divide = "/"
    Equal = "="
    Underbar = "_"
SpecialSymbol = SpecialSymbol()

class CaseController:
    def Camel(self, stringList):
        newString = ""
        for i in range(1, len(stringList)):
            stringList[i] = stringList[i].capitalize()
        for i in range(len(stringList)):
            newString += stringList[i]
        return newString


    def EliminateSpace(self, stringList):
        newString = ""
        for i in range(len(stringList)):
            newString += stringList[i]
        return newString

CaseController = CaseController()




def typePrint(*StringToPrint):
    if StringToPrint[0] == "":
        typeInput("printf(\"\");")
        Cursor.Left(5)
    else:
        typeInput("printf(\""+StringToPrint[0]+"\\"+"n\""+");"+"\n")

def defineVariable(*varstats):
    #*varstats = [Type, Case, Name, InitValue]
    Type = 0
    Case = 1
    Name = 2
    InitValue = 3
    if(varstats[Case] == "none"):
        varName = CaseController.EliminateSpace(varstats[Name])
    elif(varstats[Case] == "Camel"):
        varName = CaseController.Camel(varstats[Name])
    else:
        varName = CaseController.EliminateSpace(varstats[Name])

    typeInput(varstats[Type] + " " + varName)

    if(len(varstats) == 4):
        typeInput(" = " + varstats[3])

    typeInput(";\n")

#def defineFunction(*func):


def typeClassicIf(initialCondition, terminalCondition, changeCondition):
    typeInput("if("+initialCondition+";"+terminalCondition+";"+changeCondition+"){}")
    Cursor.Left(1)


def typeRepsIf(reps):
    typeInput("if(int i = 0; i < "+reps+"; i++){}")
    Cursor.Left(1)

def typeElse():
    typeInput("else{}")
    Cursor.Left(1)




'''
def moveCursorLeft(amountToMoveCursor):
        for i in range(amountToMoveCursor):
                keyboard.press(Key.left)

def moveCursorRight(amountToMoveCursor):
        for i in range(amountToMoveCursor):
                keyboard.press(Key.right)

def moveCursorUp(amountToMoveCursor):
    for i in range(amountToMoveCursor):
        keyboard.press(Key.up)

def moveCursorDown(amountToMoveCursor):
    for i in range(amountToMoveCursor):
        keyboard.press(Key.down)
'''
