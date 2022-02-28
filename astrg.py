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

    def rmchild(self,child):
        return self.children.remove(child)

    def rmchildidx(self,chidx):
        return self.children.pop(chidx)

    def setval(self,key:str,value : Any):
        self.value[key] = value

    def getval(self,key:str,value : Any):
        self.value[key] = value

    def toany3(self,parent = None) -> Node:
        if not parent:
            parent = Node(self.label)

        for i in range(0,len(self.children)):
            child : ASTNode  = self.children[i]
            ca3 = Node(child.label,parent=parent)
            if child.getval("d"):
                Node(child.getval("d"),parent=ca3)
            else:
                child.toany3(ca3)
        
        return parent
