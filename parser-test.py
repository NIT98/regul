from parso import parse
from lexrg import LexerRegul
lex = LexerRegul("/^[0-9]+$/")

print("#Test Parse Nethod :")
parse(lex)
