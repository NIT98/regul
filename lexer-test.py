from lexrg import LexerRegul
lex = LexerRegul("/^[0-9]+$/")

print("start",lex.start())
print("end",lex.end())
print(lex.nextc())
print(lex.nextc())
print(lex.nextc())
print(lex.prevc())
print(lex.prevc())
c = lex.nextc()
while c != '':
    print(c)
    c = lex.nextc()

print(lex.eoi())
