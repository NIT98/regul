class LexerRegul:
    def __init__(self,input) -> None:
        self.input = input
        self.pos = 0

    def nextc(self) -> str:
        if len(self.input) <= self.pos:
            return ''

        c = self.input[self.pos] 
        self.pos += 1

        return c

        