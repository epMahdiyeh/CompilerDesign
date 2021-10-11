import re
import os
#def getNextToken():

def cur_state(state:int,char:str):
    symbol = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-" ,"*", "<"]
    whitespace = [" ", "\n", "\t", "\r", "\f", "\v"]
    keywords = ["if", "else", "void", "int", "repeat", "break", "until", "return"]
    out = [False, "next_state or error type", False]

    if (state == 0):
        # keyword an id
        if(re.match(char,'[a-zA-Z]')):
            out[1]=1
        #num
        elif(re.match(char,'[0-9]')):
            out[1]=3
        #=
        elif(re.match(char=="=")):
            out[1]=4
        #symbol exept for =
        elif(char in symbol):
            out[1]=7
        #comment
        elif(char=='/'):
            out[1]=8
        #whitespace
        elif(char in whitespace):
            out[1]=14





