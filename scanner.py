import re
import os
def getNextToken():

def cur_state(state:int,char:str):
    symbol = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "<"]
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
        elif(char=='*'):
            out=2
        #=
        elif(char=='='):
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
#id
    elif(state==1):
        if(re.match(char,'[a-zA-Z0-9]')):
            out = 1
        elif(char in whitespace+symbol + ["=", "*", "/"]):
            out =15
            end = True
        else:
            error=True
            out="invalid input"
    elif(state==2):
        if(char=='/'):
            error=True
            out="unmatched comment"
        else:
            out=7

#num
    elif(state==3):
        if(re.match(char,'[0-9]')):
            out=3
        elif((char in whitespace+symbol+["=", "*", "/"]) or (re.match(char,'[a-zA-z]'))):
            out=16
            end=True
        else:
            out="invalid number"
            error=True
# =
    elif(state==4):
        if(char=='='):
            out=5
        elif(char in whitespace+symbol+[ "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            out=6
            end=True
        else:
            error = True
            out = "invalid input"
#==
    elif(state==5):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            out=17
        else:
            error=True
            out="invalid input"
#symbol
    elif(state==7):
        if(char in whitespace+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]') ):
            out=18
        else:
            error=True
            out="invalid input"
#
    elif(state==8):
        if( char=='*'):
            out=9
        elif(char=='/'):
            out=12
        else:
            out="invalid input"
            error=True
    elif(state==9) :
        if( not char=='*'):
            out=9
        elif(char=='*'):
            out=10
        else:
            out = "unclosed comment"
            error = True
    elif(state==10):
        if(char=='/'):
            out=11
        else:
            out = "invalid input"
            error = True

    elif(state==11):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            out=21
        else:
            out = "invalid input"
            error = True
    elif(state==12) :
        if(not char=="\n"):
            out=12
        else:
            out=13
    elif(state==13):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            out=20
        else:
            out = "invalid input"
            error = True









