from loging import logtree
from parsrg import parse
from lexrg import LexerRegul as Lexer
from utils import toany3d

print("#Test Parse Method :")
root = parse(Lexer("/^([^a-z]+|P){0,1}$/"))
logtree(toany3d(root))