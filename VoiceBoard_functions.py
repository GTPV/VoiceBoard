from pynput.keyboard import Key,Controller
keyboard = Controller()


def typeInput(stringToType):
    keyboard.type(stringToType)

class CursorController:
        def Left(self, amountToMoveCursor):
                for i in range(amountToMoveCursor):
                        keyboard.press(Key.left)
        def Right(self, amountToMoveCursor):
                for i in range(amountToMoveCursor):
                        keyboard.press(Key.right)
        def Up(self, amountToMoveCursor):
                for i in range(amountToMoveCursor):
                        keyboard.press(Key.up)
        def Down(self, amountToMoveCursor):
                for i in range(amountToMoveCursor):
                        keyboard.press(Key.down)

Cursor = CursorController()




def typePrint(*StringToPrint):
    if StringToPrint[0] == "":
        typeInput("printf(\"\\n\");")
        Cursor.Left(5)
    else:
        typeInput("printf(\"" + StringToPrint[0] + "\n\");")

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
