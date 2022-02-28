from operator import eq, le,ne
from lexrg import LexerRegul
from loging import errexpec

spec = ["[","]","(",")","{","}",".","+","*","?","|"]

def parse(lex:LexerRegul):
    if eq(lex.start(),"^"):
        print("is start")
        lex.nextc()

    if eq(lex.end(),"$"):
        print("is end")
        lex.dwnbound()

    regex(lex)

    print("accepted!")
    print(lex.input)

def regex(lex : LexerRegul):
    if lex.eoi():
        print("eoi")
        return

    expr(lex)
    regex(lex)

def expr(lex : LexerRegul):
    exprpost(lex)

def exprpost(lex : LexerRegul):
    exprprim(lex)
    
    c = lex.nextc()
    if eq(c,"+"):
        print("plus",lex.curc())     
    elif eq(c,"?"):
        print("ignore")        
    elif eq(c,"*"):
        print("more than 0")        
    elif eq(c,"|"):
        print("union")        
        expr(lex)
    elif eq(c,"{"):
        print("sizing")        
        sizing(lex)
        if ne(lex.nextc(),"}"):
            errexpec("}",lex.pos)
        print("end sizing")        
    else:
        lex.prevc()

def exprprim(lex : LexerRegul):
    c = lex.nextc()
    print("mirp",{c})
    if eq(c,"."):
        print("any")        
    elif eq(c,"("):
        print("group")
        print("------------------")
        expr(lex)
        print("lex.curc()",lex.curc())
        print("------------------")
        if ne(lex.nextc(),")"):
            errexpec(")",lex.pos)
    
    elif eq(c,"["):
        if eq(lex.curc(),"^"):
            lex.nextc()
            print("notset")
        else:
            print("set")

        item(lex)

        if ne(lex.nextc(),"]"):
            errexpec("]",lex.pos)
    else:
        print({c})
        if c in ["+","-","*","?","{","|"]:
            lex.prevc()

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
    print("set end")

def range(lex : LexerRegul):
    ch(lex)

    if eq(lex.curc(),"-"):
        lex.nextc()
        ch(lex)
        print("is range")

def digit(lex : LexerRegul):
    c = lex.nextc()
    t = ''
    while c.isnumeric():
        t += c
        c = lex.nextc()

    print("digit",t)
    lex.prevc()

def ch(lex : LexerRegul):
    print("ch",lex.nextc())
