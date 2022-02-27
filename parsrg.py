from lexrg import LexerRegul

def parse(lex : LexerRegul):
    if lex.nextc() != "/":
        print("error : pattern must start with '/'")
    
    ast = regex(lex)
    
    if lex.nextc() != "/":
        print("error : pattern must end with '/'")
    
    return ast

def regex(lex : LexerRegul):
    pass    

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