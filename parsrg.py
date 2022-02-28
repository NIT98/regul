from operator import eq
from lexrg import LexerRegul
from loging import errpatt, errsyntx

def parse(lex:LexerRegul):
    if lex.nextc() != "/":
        errpatt("input start with '/'")
        return
    if lex.nextc() == "^":
        #start with
        pass
    else:
        lex.prevc()
 
    regex(lex)

    if lex.nextc() == "$":
        #ended with
        pass
    else:
        lex.prevc()
 
    if lex.nextc() != "/":
        errpatt("input end with '/'")
        return

    print("accepted!")

def regex(lex : LexerRegul):
    # lex.pos = len(lex.input) - 1
    if lex.eoi():
        return

    expr(lex)
    regex(lex)

def expr(lex : LexerRegul):
    c = lex.nextc()

    if c == ".":
        return
    if c == "(":
        return
    if c == "[":
        if lex.nextc() == "^":
            #not set
            pass
        else:
            #set
            lex.prevc()
    
        if not eq(lex.nextc(),"]"):
            errsyntx("expected ] on index %s",lex.pos - 1)
        return
    
    expr(lex)
    c = lex.nextc()
    
    if c == "+":
        return
    if c == "?":
        return
    if c == "*":
        return
    if c == "|":
        expr(lex)
        return
    if c == "{":
        sizing(lex)
        if not eq(lex.nextc(),"}"):
            errsyntx("expected } on index %s" % lex.pos - 1);
        return
    
def sizing(lex : LexerRegul):
    pass

def item(lex : LexerRegul):
    pass

def range(lex : LexerRegul):
    pass

def digit(lex : LexerRegul):
    pass

def ch(lex : LexerRegul):
    pass