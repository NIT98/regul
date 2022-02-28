from operator import eq

from loging import errlex, log


class LexerRegul:
    def __init__(self,input) -> None:
        self.input = input[1:-1]
        self.pos = 0

        if eq(input[0],"/"):
            log("regular expersion must started with '/'")
            exit(1)

        if eq(input[len(self.input) - 1],"/"):
            log("regular expersion must ended with '/'")
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
        return self.input[len(self.input) - 1]

    #end of input
    def eoi(self) -> str:
        return self.pos >= len(self.input)
    
    def curc(self) -> str:
        raise self.input[self.pos]