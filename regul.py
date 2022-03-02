from typing_extensions import Self
from astrg import ASTNode, AstType
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
        self.cpos = -1
        start = self.ast.getval("start")
        end = self.ast.getval("end")
        self.interpret(self.ast)
        #start match sub function
        self.rststr()

    def rststr(self):
        self.string = None
        self.cpos = -1

    def nxtcpos(self):
        self.cpos += 1
        return self.string[self.cpos]

    def prvcpos(self):
        self.cpos -= 1
        return self.string[self.cpos]

    def setcpos(self,cpos : int):
        self.cpos = cpos

    def interpret(self,ast : ASTNode):
        if ast.eqtype(AstType.REGEX):
            if len(ast.children):
                self.expr(ast.child(0))
                self.interpret(ast.child(1))
        else:
            print("interpret error ast")
    
    def expr(self,ast : ASTNode):
        pass
    def exprunion(self,ast : ASTNode):
        pass
    
    