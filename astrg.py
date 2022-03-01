from enum import Enum
from typing import Any, Dict, List
from anytree import Node, RenderTree

class AstType ( Enum ):
    SYNTAX_TREE = "stree"
    REGEX = "regex"
    EXPR = "expr"
    MORE_THAN_ONE = "+"
    MORE_THAN_ZERO = "*"
    BE_OR_NOT = "?"
    UNION = "UNION",
    CONCAT = "concact",
    GROUP = "group",
    POST_SIZING = "POST_SIZING"
    SIZING = "sizing"
    ANY = ".",
    START = "^",
    END = "$",
    ITEM_SET = "set",
    ITEM_NOSET = "notset",
    ITEM = "item",
    RANGE = "range",
    CH = "ch",
    DIGIT = "digit"

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

    def addchild(self,child):
        self.children.append(child)

    def child(self,index : int ):
        return self.children[index]

    def rmchild(self,child):
        return self.children.remove(child)

    def rmchildidx(self,chidx):
        return self.children.pop(chidx)

    def setval(self,key:str,value : Any):
        self.value[key] = value

    def getval(self,key:str):
        return self.value.get(key)
    
    def eqtype(self,type:AstType):
        return self.type == type