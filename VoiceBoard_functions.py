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


def closeCurlyBracket():
    typeInput("}")





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
            keyboardPress(KeyToPress)
class PseudoCursorController:
    def Left(self, amountToMoveCursor):
        self.Move(amountToMoveCursor, 'Key.left')
    def Right(self, amountToMoveCursor):
        self.Move(amountToMoveCursor, 'Key.right')
    def Up(self, amountToMoveCursor):
        self.Move(amountToMoveCursor, 'Key.up')
    def Down(self, amountToMoveCursor):
        self.Move(amountToMoveCursor, 'Key.down')
    def Move(self, amountToMoveCursor, KeyToPress):
        for i in range(amountToMoveCursor):
            print(KeyToPress)
Cursor = PseudoCursorController()



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


    def MergeWithoutSpace(self, stringList):
        newString = ""
        for i in range(len(stringList)):
            newString += stringList[i]
        return newString

    def MergeAddSpace(self, stringList):
        newString = ""
        if len(stringList) == 0:
            return newString
        elif len(stringList) == 1:
            return stringList[0]
        for i in range(len(stringList)-1):
            newString += stringList[i]
            newString += " "
        newString += stringList[-1]
        return newString
CaseController = CaseController()




def typePrint(*StringToPrint):
    if StringToPrint[0] == "":
        typeInput("printf(\"\");")
        Cursor.Left(3)
    else:
        typeInput("printf(\""+StringToPrint[0]+"\\"+"n\""+");"+"\n")

def defineVariable(*varstats):
    #*varstats = [Type, Case, Name, InitValue]
    Type = 0
    Case = 1
    Name = 2
    InitValue = 3
    if(varstats[Case].lower() == "none"):
        varName = CaseController.MergeWithoutSpace(varstats[Name])
    elif(varstats[Case].lower() == "camel"):
        varName = CaseController.Camel(varstats[Name])
    else:
        varName = CaseController.MergeWithoutSpace(varstats[Name])

    typeInput(varstats[Type] + " " + varName)

    if(len(varstats) == 4):
        varInitValue = CaseController.MergeAddSpace(varstats[3])
        typeInput(" = " + varInitValue)

    typeInput(";\n")

#def defineFunction(*func):


def typeClassicFor(*conditions):
    Initial = 0
    Terminal = 1
    Change = 2
    typeInput("for("+CaseController.MergeAddSpace(conditions[Initial])+";"+CaseController.MergeAddSpace(conditions[Terminal])+";"+CaseController.MergeAddSpace(conditions[Change])+"){")
    #Cursor.Left(1)


def typeRepsFor(reps):
    typeInput("for(int i = 0; i < "+reps+"; i++){")
    #Cursor.Left(1)

def typeIf(*condition):
    if(condition == ()):
        typeInput("if(){")
        #Cursor.Left(1))
    else:
        typeInput("if(" + condition[0] + "){")
        #Cursor.Left(1)

def typeElse():
    typeInput("else{")
    #Cursor.Left(1)




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
