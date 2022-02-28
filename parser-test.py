from loging import logtree
from parsrg import parse
from lexrg import LexerRegul as Lexer

print("#Test Parse Method :")
root = parse(Lexer("/^([^a-z]+|P){0,1}$/"))

logtree(root.toany3())