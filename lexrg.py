from utils import neq
from loging import errlex

class LexerRegul:
    def __init__(self,input) -> None:
        self.input = input[1:-1]
        self.pos = 0
        self.bound = len(self.input) 
        if neq(input[0],"/"):
            errlex("regular expersion must started with '/'")
            exit(1)

        if neq(input[self.bound + 1],"/"):
            errlex("regular expersion must ended with '/'")
            exit(1)
            
    def nextc(self) -> str:
        if self.eoi():
            return ''

        c = self.input[self.pos] 
        self.pos += 1

        return c

    def prevc(self) -> str:
        if self.pos < 1:
            return None

        self.pos -= 1
        return self.input[self.pos]

    def start(self) -> str:
        return self.input[0]

    def end(self) -> str:
        return self.input[self.bound - 1]

    #end of input
    def eoi(self) -> str:
        return self.pos >= self.bound
    
    def curc(self) -> str:
        return self.input[self.pos]
    
    def upbound(self):
        self.bound += 1
    
    def dwnbound(self):
        self.bound -= 1
    