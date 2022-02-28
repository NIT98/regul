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
    exprunion(lex)

def exprunion(lex: LexerRegul):
    exprpost(lex)

    if eq(lex.curc(), "|"):
        lex.nextc()
        expr(lex)

def exprpost(lex : LexerRegul):
    exprprim(lex)
    
    if unaryoprator(lex):
        lex.nextc()
    elif eq(lex.curc(),"{"):
        exprsize(lex)

def exprsize(lex : LexerRegul):
    print("sizing")        
   
    if ne(lex.nextc(),"{"):
        errexpec("{",lex.pos)

    sizing(lex)
    
    if ne(lex.nextc(),"}"):
        errexpec("}",lex.pos)

def unaryoprator(lex : LexerRegul):
    return lex.curc() in ["+","*","?"]

def exprprim(lex : LexerRegul):
    c = lex.curc()

    if eq(c,"("):
        exprgroup(lex)
    elif eq(c,"["):
        exprset(lex)
    elif eq(c,"."):
        exprany(lex)
    else:
        lex.nextc()
    

def exprgroup(lex : LexerRegul):
    print("group")        
    if ne(lex.nextc(),"("):
        errexpec("(",lex.pos)

    expr(lex)
    
    if ne(lex.nextc(),")"):
        errexpec(")",lex.pos)

def exprany(lex : LexerRegul):
    lex.nextc()

def exprset(lex : LexerRegul):
    if ne(lex.nextc(),"["):
        errexpec("]",lex.pos)
    
    if eq(lex.curc(),"^"):
        lex.nextc()
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
