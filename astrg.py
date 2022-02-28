from enum import Enum
from typing import Any, Dict, List

class AstType ( Enum ):
    pass

class ASTNode():
    label : str
    type : AstType
    children : List
    value : Dict
    def __init__(self,label : str,type : AstType) -> None:
        self.label = label
        self.type = type
        self.children = [] 
        self.value = dict()

    