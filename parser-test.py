from traceback import print_list
from parsrg import parse
from lexrg import LexerRegul as Lexer

print("#Test Parse Method :")
parse(Lexer("/^([^a-z]+|P){0,1$/"))
# parse(Lexer("/^[0-9]+$/"))
# parse(Lexer("0/^[0-9]+$/"))
# parse(Lexer("/^[0-9]+$/0"))
