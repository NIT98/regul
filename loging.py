from anytree import Node, RenderTree

def log(title : str,message : any):
    print("%s : %s" %(title,message))

def errlex(msg : any):
    log("lexical error",msg)

def errsyntx(msg : any):
    log("syntax error",msg)

def errpatt(msg : any):
    log("pattern error",msg)

def errexpec(token:str,index : int):
    errpatt("expected '%s' on index %s" % (token,index))

def logtree(root : Node):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
