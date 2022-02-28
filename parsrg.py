from lexrg import LexerRegul
from loging import errpatt

def parse(lex : LexerRegul):
    if lex.nextc() != "/":
        errpatt("input start with '/'")
        exit(1)
    
    ast = regex(lex)
    
    if lex.nextc() != "/":
        errpatt("input end with '/'")
        exit(1)

    return ast

def regex(lex : LexerRegul):
    lex.pos = len(lex.input) - 1

def expr(lex : LexerRegul):
    pass

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