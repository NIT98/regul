from traceback import print_list
from parsrg import parse
from lexrg import LexerRegul as Lexer

print("#Test Parse Method :")
parse(Lexer("/^[0-9]+$/"))
parse(Lexer("0/^[0-9]+$/"))
parse(Lexer("/^[0-9]+$/0"))
