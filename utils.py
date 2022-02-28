from anytree import Node

from astrg import ASTNode

def eq(a,b):
    return a == b
def neq(a,b):
    return not (a == b)

def toany3d(parent : ASTNode) -> Node: 
    root = Node(parent.label)

    for i in range(0,len(parent.children)):
        child : ASTNode  = parent.children[i]
        ca3 = Node(child.label,parent=root)
        d = child.value("d")
        if d:
            Node(d,parent=ca3)

        child.toany3(ca3)

    return root
