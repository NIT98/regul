from typing_extensions import Self
from astrg import ASTNode
from lexrg import LexerRegul
from parsrg import parse

class Regul:
    
    def __init__(self,ast : ASTNode) -> None:
        self.ast = ast
        self.string = None
        self.cpos = -1

    def compile(pattern:str) -> Self:
        lex = LexerRegul(pattern)
        prs = parse(lex)
        return Regul(prs)

    def match(self,string : str):
        self.string = string
        self.cpos = 0
        #start match sub function
        self.rststr()

    def rststr(self):
        self.string = None
        self.cpos = -1

    def nxtcpos(self):
        self.cpos += 1

    def prvcpos(self):
        self.cpos -= 1

    def setcpos(self,cpos : int):
        self.cpos = cpos

    def interpret(self,ast : ASTNode):
        pass
    
    def expr(self,ast : ASTNode):
        pass
    