from operator import eq, le,ne
import re
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

def regex(lex : LexerRegul) -> ASTNode:
    regast = ASTNode("regex",AstType.REGEX)
    if lex.eoi():
        return regast

    regast.addchild(expr(lex))
    regast.addchild(regex(lex))

def expr(lex : LexerRegul):
    return exprunion(lex)

def exprunion(lex: LexerRegul) -> ASTNode:
    past = exprpost(lex)

    if eq(lex.curc(), "|"):
        lex.nextc()
        uast = ASTNode("union",AstType.UNION)
        uast.addchild(past)
        uast.addchild(expr(lex))
        return uast 

    return past

def totype(v : str):
    if eq(v,"+"):
        return AstType.MORE_THAN_ONE
    if eq(v,"*"):
        return AstType.MORE_THAN_ZERO
    if eq(v,"?"):
        return AstType.BE_OR_NOT
    return None

def exprpost(lex : LexerRegul) -> ASTNode:
    past = exprprim(lex)
    if unaryoprator(lex):
        ctype = lex.nextc()
        unast = ASTNode("unary",totype(ctype))
        unast.addchild(past)
        return unast

    elif eq(lex.curc(),"{"):
        sast = ASTNode("expr",AstType.SIZING)
        sast.addchild()
        return exprsize(lex)

    else:
        return past

def exprsize(lex : LexerRegul) -> ASTNode:
   
    if ne(lex.nextc(),"{"):
        errexpec("{",lex.pos)

    sast = sizing(lex)
    
    if ne(lex.nextc(),"}"):
        errexpec("}",lex.pos)

    return sast

def unaryoprator(lex : LexerRegul):
    return lex.curc() in ["+","*","?"]

def exprprim(lex : LexerRegul) -> ASTNode:
    c = lex.curc()

    if eq(c,"("):
        return exprgroup(lex)
    elif eq(c,"["):
        return exprset(lex)
    elif eq(c,"."):
        return exprany(lex)
    
    return ch(lex)

def exprgroup(lex : LexerRegul):
    print("group")        
    if ne(lex.nextc(),"("):
        errexpec("(",lex.pos)

    expr(lex)
    
    if ne(lex.nextc(),")"):
        errexpec(")",lex.pos)

def exprany(lex : LexerRegul):
    lex.nextc()
    return ASTNode("expr",AstType.ANY)

def exprset(lex : LexerRegul):
    
    if ne(lex.nextc(),"["):
        errexpec("]",lex.pos)
    
    type : AstType    
    if eq(lex.curc(),"^"):
        lex.nextc()
        type = AstType.ITEM_NOSET
    else:
        type = AstType.ITEM_SET

    setast = ASTNode("expr",type) 

    setast.addchild(item(lex))

    if ne(lex.nextc(),"]"):
        errexpec("]",lex.pos)

    return setast

def sizing(lex : LexerRegul):
    szast = ASTNode("sizing",AstType.SIZING)
    if lex.curc().isnumeric():
        szast.addchild(digit(lex))
    
    if eq(lex.curc(),","):
        lex.nextc()
        szast.addchild(digit(lex))

    return szast

def item(lex : LexerRegul):
    itast = ASTNode("item",AstType.ITEM)
    while ne(lex.curc(),"]"):  
        itast.addchild(range(lex))

    return itast

def range(lex : LexerRegul) -> ASTNode:
    chast = ch(lex)

    if eq(lex.curc(),"-"):
        lex.nextc()
        rast = ASTNode("range",AstType.RANGE)
        rast.addchild(chast)
        rast.addchild(ch(lex))
        return rast

    return chast
def digit(lex : LexerRegul) -> ASTNode:
    c = lex.nextc()
    t = ''
    while c.isnumeric():
        t += c
        c = lex.nextc()

    lex.prevc()

    if t:
        ast = ASTNode("ch",AstType.CH)
        ast.setval("d",t)
        return ast
    
    return None 

def ch(lex : LexerRegul) -> ASTNode:
    ast = ASTNode("ch",AstType.CH)
    ast.setval("d",lex.nextc())
    return ast
