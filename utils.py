from anytree import Node

from astrg import ASTNode

def eq(a,b):
    return a == b
def neq(a,b):
    return not (a == b)
def toany3d(root : ASTNode,parent=None) -> Node: 
    
    if not parent:
        parent = Node("root")

    for i in range(0,len(root.children)):
        child : ASTNode  = root.children[i]
        ca3 = Node(child.label,parent=parent)
        d = child.getval("d")
        if d:
            Node(d,parent=ca3)

        toany3d(child,ca3)

    return parent