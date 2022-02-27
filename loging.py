
def log(title : str,message : any):
    print("%s:%s" %(title,message))

def errlex(msg : any):
    log("lexical error",msg)

def errsyntx(msg : any):
    log("syntax error",msg)

def errpatt(msg : any):
    log("pattern error",msg)

