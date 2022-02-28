from operator import eq,ne
from lexrg import LexerRegul
from loging import errexpec

def parse(lex:LexerRegul):
    if eq(lex.start(),"^"):
        print("is start")
        lex.nextc()

    if eq(lex.end(),"$"):
        print("is end")
        lex.dwnbound()

    regex(lex)

    print("accepted!")

def regex(lex : LexerRegul):
    # lex.pos = len(lex.input) - 1
    if lex.eoi():
        print("end of input")
        return

    expr(lex)
    regex(lex)

def expr(lex : LexerRegul):
    exprpost(lex)

def exprpost(lex : LexerRegul):
    exprprim(lex)
        
    c = lex.nextc()
    
    if eq(c,"+"):
        print("plus")        
    elif eq(c,"?"):
        print("ignore")        
    elif eq(c,"*"):
        print("more than 0")        
    elif eq(c,"|"):
        print("union")        
        expr(lex)
    elif eq(c,"{"):
        print("start sizing")        
        sizing(lex)
        exit(1)
        if ne(lex.nextc(),"}"):
            errexpec("}",lex.pos)
        print("end sizing")        
    else:
        lex.prevc()

def exprprim(lex : LexerRegul):
    c = lex.nextc()
    print("c",c)
    if eq(c,"."):
        print("any")        
    if eq(c,"("):
        print("group")
        expr(lex)
        if ne(lex.nextc(),")"):
            errexpec(")",lex.pos)
    
    if eq(c,"["):
        if eq(lex.curc(),"^"):
            print("notset")
        else:
            print("set")

        item(lex)

        if ne(lex.nextc(),"]"):
            errexpec("]",lex.pos)

def sizing(lex : LexerRegul):
    if lex.curc().isnumeric():
        digit(lex)
        print("size min")
    
    if eq(lex.curc(),","):
        lex.nextc()
        digit(lex)
        print("size max")

def item(lex : LexerRegul):
    while ne(lex.curc(),"]"):  
        range(lex)

def range(lex : LexerRegul):
    ch(lex)

    if eq(lex.nextc(),"-"):
        print("is range")
        ch(lex)

def digit(lex : LexerRegul):
    c = lex.nextc()
    t = ''
    while c.isnumeric():
        t += c
        c = lex.nextc()

    print("digit",t)
    lex.prevc()

def ch(lex : LexerRegul):
    lex.nextc()