"""
Daniela Tamez   A01197468

26/04/23
Proyecto Compiladores

Tutorial Consultado: 
https://medium.com/@marcelogdeandrade/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
"""

from lexer import Lexer
from parser_1 import Parser

fname = "pruebaFor.txt"
with open(fname) as f:
    text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()