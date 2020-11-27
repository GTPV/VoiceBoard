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
    #keyboard.type(stringToType)
    print(stringToType)

def keyboardPress(KeyToPress):
    keyboard.press(KeyToPress)
    print(KeyToPress)

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




def typePrint(*StringToPrint):
    if StringToPrint[0] == "":
        typeInput("printf(\"\");")
        Cursor.Left(5)
    else:
        typeInput("printf(\""+StringToPrint[0]+"\\"+"n\""+");")

def defineVariable(variableType, variableName):
        typeInput(variableType+" = "+variableName)


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
