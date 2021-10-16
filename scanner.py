import re
import os
#def getNextToken():

def cur_state(state:int,char:str):
    symbol = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-" ,"*", "<"]
    whitespace = [" ", "\n", "\t", "\r", "\f", "\v"]
    keywords = ["if", "else", "void", "int", "repeat", "break", "until", "return"]
    out =  ["next_state or error type"]
    error=False
    end=False
    if (state == 0):
        # keyword an id
        if(re.match(char,'[a-zA-Z]')):
            out = 1
        #num
        elif(re.match(char,'[0-9]')):
            out = 3
        #=
        elif(re.match(char=="=")):
            out = 4
        #symbol exept for =
        elif(char in symbol):
            out = 7
        #comment
        elif(char=='/'):
            out=8
        #whitespace
        elif ( char in whitespace ) :
            out = 14
        else:
         error=True
         out="Invalid input"
    elif(state==1):
        if(re.match(char,'[a-zA-Z0-9]')):
            out=1
        elif(char in whitespace+symbol+'='):
            out=15
            end = True
        else:
            error=True
            out="invalid input"
    elif(state==3):
        if(re.match(char,'[0-9]')):
            out=3
        elif((char in whitespace+symbol+'=') or (re.match(char,'[a-zA-z]'))):
            out=16
            end=True
        else:
            out="invalid number"









