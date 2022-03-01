from typing_extensions import Self
from astrg import ASTNode
from parsrg import parse

class Regul:
    def __init__(self,ast : ASTNode) -> None:
        self.ast = ast

    def compile(pattern:str) -> Self:
        return Regul(parse(pattern))
