from operator import eq
from lexrg import LexerRegul
from loging import errexpec, errpatt, errsyntx

def parse(lex:LexerRegul):
    if lex.nextc() != "/":
        errexpec("/",lex.pos)
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
        errexpec("/",lex.pos)
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

        item(lex)

        if not eq(lex.nextc(),"]"):
            errexpec("]",lex.pos)
        return
    
    lex.prevc()

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
            errexpec("}",lex.pos)
        return

    if c != '':
        errsyntx("pattern is not valid")

def sizing(lex : LexerRegul):
    if lex.curc().isnumeric():
        digit(lex)
    
    if eq(lex.curc(),","):
        digit(lex)

def item(lex : LexerRegul):
    c = lex.nextc()
    while not eq(c,"]"):  
        range(lex)

def range(lex : LexerRegul):
    ch(lex)

    if eq(lex.nextc(),"-"):
        ch(lex)

def digit(lex : LexerRegul):
    c = lex.nextc()
    t = ''
    while c.isnumeric():
        t += c
        c = lex.nextc()

    lex.nextc()

def ch(lex : LexerRegul):
    lex.nextc()