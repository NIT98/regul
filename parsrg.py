from operator import eq, le,ne
from astrg import ASTNode, AstType
from lexrg import LexerRegul
from loging import errexpec

def parse(lex:LexerRegul) -> ASTNode:
    root = ASTNode("syntax-tree",AstType.SYNTAX_TREE)
    if eq(lex.start(),"^"):
        lex.nextc()
        root.setval("start",True)

    if eq(lex.end(),"$"):
        lex.dwnbound()
        root.setval("end",True)

    root.addchild(regex(lex))

    return root

def regex(lex : LexerRegul):
    regast = ASTNode("regex",AstType.REGEX)
    if lex.eoi():
        return regast

    regast.addchild(expr(lex))
    regast.addchild(regex(lex))

def expr(lex : LexerRegul):
    exprunion(lex)

def exprunion(lex: LexerRegul):
    exprpost(lex)

    if eq(lex.curc(), "|"):
        print("union")
        lex.nextc()
        expr(lex)

def exprpost(lex : LexerRegul):
    exprprim(lex)
    if unaryoprator(lex):
        print("opr")
        lex.nextc()
    elif eq(lex.curc(),"{"):
        exprsize(lex)
    else:
        print("post")

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
    print("prim")
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
