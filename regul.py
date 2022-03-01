from typing_extensions import Self
from astrg import ASTNode
from lexrg import LexerRegul
from parsrg import parse

class Regul:
    def __init__(self,ast : ASTNode) -> None:
        self.ast = ast

    def compile(pattern:str) -> Self:
        lex = LexerRegul(pattern)
        prs = parse(lex)
        return Regul(prs)
    
