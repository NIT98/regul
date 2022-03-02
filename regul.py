from typing_extensions import Self
from astrg import ASTNode, AstType
from lexrg import LexerRegul
from parsrg import parse

posttype = [AstType.MORE_THAN_ZERO,AstType.MORE_THAN_ONE,AstType.BE_OR_NOT]

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
        self.exprunion(ast)
    
    def exprunion(self,ast : ASTNode):
        if not ast.eqtype(AstType.UNION):
            self.exprunary(ast)
        else:
            self.expr(ast.child(0))
            self.expr(ast.child(1))
   
    def exprunary(self,ast : ASTNode):
        if not ast.type in posttype:
            self.exprsize(ast)
        else:
            opr = ast.type
            self.expr(ast.child(0))
    
    def exprsize(self,ast : ASTNode):
        if not ast.eqtype(AstType.POST_SIZING):
            self.exprgoup(ast)
        else:
            self.expr(ast.child(0))
            self.expr(ast.child(1))
   
    def exprgoup(self,ast : ASTNode):
        if not ast.eqtype(AstType.GROUP):
            self.exprset(ast)
        else:
            self.expr(ast.child(0))

    def exprset(self,ast : ASTNode):
        if not ast.eqtype(AstType.ITEM_SET):
            self.exprany(ast)
        else:
            isnot = ast.getval("d")
            self.expr(ast.child(0))

    def exprany(self,ast : ASTNode):
        if not ast.eqtype(AstType.ANY):
            self.item(ast)
        else:
            pass

    def item(self,ast : ASTNode):
        if not ast.eqtype(AstType.ITEM):
            self.sizing(ast)
        else:
            for sit in ast.children:
                self.expr(sit)

    def sizing(self,ast : ASTNode):
        if not ast.eqtype(AstType.POST_SIZING):
            self.range(ast)
        else:
            ch1 : ASTNode = ast.child(0) 
            ch2 : ASTNode = ast.child(1)
            min = ch1.getval("d")
            max = ch2.getval("d")
   
    def range(self,ast : ASTNode):
        if not ast.eqtype(AstType.POST_SIZING):
            self.exprunary(ast)
        else:
            ch1 : ASTNode = ast.child(0) 
            ch2 : ASTNode = ast.child(1)
            l = ord(ch1.getval("d"))
            r = ord(ch2.getval("d"))
 
    def ch(self,ast : ASTNode):
        if ast.eqtype(AstType.CH):
            pass