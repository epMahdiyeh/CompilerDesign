import re
import os

def is_keyword (KEYWORDS, ID : str):
    if (ID in KEYWORDS):
        return True
    else:
        return False
def lookahead_state(state:int,char:str):
    symbol = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "<"]
    whitespace = [" ", "\n", "\t", "\r", "\f", "\v"]
    keywords = ["if", "else", "void", "int", "repeat", "break", "until", "return"]
    position =  "next_state or error type"
    error=False
    end=False

    INPUT = open(os.path.realpath("./input/input.txt"), "rb")
    errors = open(os.path.realpath("./ResultFiles/lexical_errors.txt"), "w")
    symbols = open(os.path.realpath("./ResultFiles/symbol_table.txt"), "w")
    tokens = open(os.path.realpath("./ResultFiles/tokens.txt"), "w")

    add_symbols(symbols, KEYWORDS, 1)

    line = 1
    exist_error = False
    change_line = False
    first_line = True

    while (True):
        token = get_next_token(INPUT, KEYWORDS)

        if (token[3] and token[2] == -1):
            break

        if (not (token[0] == "Invalid input" or token[0] == "Unclosed comment" or token[0] == "Invalid number" or token[
            0] == "Unmatched comment" or token[0] == "COMMENT" or token[0] == "WHITESPACE")):
            if (first_line or change_line):
                if (not line == 1 and not first_line):
                    tokens.write("\n")
                tokens.write(str(line) + ".\t")
                change_line = False
                first_line = False
            tokens.write("(" + token[0] + ", " + token[1] + ")" + " ")
        elif (not (token[0] == "COMMENT" or token[0] == "WHITESPACE")):
            exist_error = True
            # -----------------------------------------------------------------------------------------unclosed comment-----------------------------------------------------------------
        # if (token[0] == "Unclosed comment"):
        # token[1] = format_unclosed_comment(token[1])
        # errors.write(str(line) + ".\t" + "(" + token[1] + ", " + token[0] + ")\n")

        if (token[0] == "ID" and token[1] not in ID):
            ID.append(token[1])

        if (token[2] > 0):
            line += token[2]
            change_line = True

    if (not exist_error):
        errors.write("There is no lexical error.")

    add_symbols(symbols, ID, 11)

    INPUT.close()
    tokens.close()
    errors.close()
    symbols.close()

    if (state == 0):
        # keyword an id
        if(re.match(char,'[a-zA-Z]')):
            position = 1
        #num
        elif(re.match(char,'[0-9]')):
            position = 3
        elif(char=='*'):
            position=2
        #=
        elif(char=='='):
            position = 4
        #symbol exept for =
        elif(char in symbol):
            position = 7
        #comment
        elif(char=='/'):
            position=8
        #whitespace
        elif ( char in whitespace ) :
            position = 14
        else:
         error=True
         position="Invalid input"
#id
    elif(state==1):
        if(re.match(char,'[a-zA-Z0-9]')):
            position = 1
        elif(char in whitespace+symbol + ["=", "*", "/"]):
            position =15
            end = True
        else:
            error=True
            position="invalid input"
    elif(state==2):
        if(char=='/'):
            error=True
            position="unmatched comment"
        else:
            position=7

#num
    elif(state==3):
        if(re.match(char,'[0-9]')):
            position=3
        elif((char in whitespace+symbol+["=", "*", "/"]) or (re.match(char,'[a-zA-z]'))):
            position=16
            end=True
        else:
            position="invalid number"
            error=True
# =
    elif(state==4):
        if(char=='='):
            position=5
        elif(char in whitespace+symbol+[ "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            position=6
            end=True
        else:
            error = True
            position = "invalid input"
#==
    elif(state==5):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            position=17
        else:
            error=True
            position="invalid input"
#symbol
    elif(state==7):
        if(char in whitespace+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]') ):
            position=18
        else:
            error=True
            position="invalid input"
#
    elif(state==8):
        if( char=='*'):
            position=9
        elif(char=='/'):
            position=12
        else:
            position="invalid input"
            error=True
    elif(state==9) :
        if( not char=='*'):
            position=9
        elif(char=='*'):
            position=10
        else:
            position = "unclosed comment"
            error = True
    elif(state==10):
        if(char=='/'):
            position=11
        else:
            position = "invalid input"
            error = True

    elif(state==11):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            position=21
        else:
            position = "invalid input"
            error = True
    elif(state==12) :
        if(not char=="\n"):
            position=12
        else:
            position=13
    elif(state==13):
        if(char in whitespace+symbol+["=", "*", "/"] or re.match(char,'[a-zA-Z0-9]')):
            position=20
        else:
            position = "invalid input"
            error = True

    if (position == "next_state or error type"):
        position = state
    out=[error,position,end]
    return out
def get_next_token (INPUT, KEYWORDS):

    states = ["","", "", "", "", "", "symbol", "", "", "", "", "", "", "whitespace", "ID", "Num", "symbol", "symbol", "", "comment", "comment", "", "", "symbol" "ID", "", "NUM", "SYMBOL", "", "SYMBOL", "", "SYMBOL", "", "", "COMMENT", "", "", "WHITESPACE"]
    change_line = 0
    string = ""

    resultForToken=[]

    while (True):
        i = 1
        character = INPUT.read(i).decode()
        if (character == ""):
            break

        next_state = lookahead_state(0, character)
        if (character == "\n" and  next_state[2]==False):
            change_line += 1

        if(next_state[0]==True):
            resultForToken=[next_state[1],string+character,change_line,False]
            return resultForToken
        elif(states[next_state[1]]!=""):
            INPUT.seek(-1 * i, os.SEEK_CUR)
            if(next_state[1]==15):
                if (is_keyword(KEYWORDS, string)):
                    resultForToken=["KEYWORD", string, change_line, False]
                    return resultForToken
            resultForToken=[states[next_state[1]], string, change_line, False]
            return resultForToken
        else:
            resultForToken= [states[next_state[1]], string + character, change_line, False]
            return resultForToken
        string =+character


    if(next_state[1]==9 or next_state[1]==10 or next_state[1]==11 or next_state[1]==12 or next_state[1]==13):
        resultForToken=["unclosed comment",string,change_line,True]
        return resultForToken
    elif(states[next_state[1]]=="" and next_state[1]!=0):
        resultForToken=["invalid input",string,change_line,True]
        return resultForToken
    else:
        resultForToken=["","",-1,False]
        return resultForToken














def write_in_symbol_file(symbols, array, start_line: int):
    return True
def format_unclosed_comment(lexeme: str):
    return True



KEYWORDS = ["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return"]
ID = []




















