from operator import eq
from lexrg import LexerRegul
from loging import errexpec, errpatt, errsyntx

def parse(lex:LexerRegul):
    if lex.start() == "^":
        lex.nextc()

    if eq(lex.end(),"$"):
        lex.dwnbound()
        lex.nextc()

    regex(lex)

    print("accepted!")

def regex(lex : LexerRegul):
    # lex.pos = len(lex.input) - 1
    if lex.eoi():
        return

    expr(lex)
    regex(lex)

def expr(lex : LexerRegul):
    exprpost(lex)

def exprpost(lex : LexerRegul):
    exprprim(lex)
        
    c = lex.nextc()
    
    if eq(c,"+"):
        pass
    elif eq(c,"?"):
        pass
    elif eq(c,"*"):
        pass
    elif eq(c,"|"):
        expr(lex)
    elif eq(c,"{"):
        sizing(lex)
        if not eq(lex.nextc(),"}"):
            errexpec("}",lex.pos)
    else:
        lex.prevc()

def exprprim(lex : LexerRegul):
    c = lex.nextc()

    if eq(c,"."):
        pass
    if eq(c,"("):
        pass
    if eq(c,"["):
        if eq(lex.curc(),"^"):
            #not set
            pass
        else:
            #set
            pass

        item(lex)

        if not eq(lex.nextc(),"]"):
            errexpec("]",lex.pos)
    
def sizing(lex : LexerRegul):
    if lex.curc().isnumeric():
        digit(lex)
    
    if eq(lex.curc(),","):
        digit(lex)

def item(lex : LexerRegul):
    while not eq(lex.curc(),"]"):  
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

    lex.prevc()

def ch(lex : LexerRegul):
    lex.nextc()