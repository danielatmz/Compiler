from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Program 
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('MAIN', r'main')
        self.lexer.add('END', r'end')

        # Print
        self.lexer.add('PRINT', r'print')

        # Parenthesis
        self.lexer.add('LPAREN', r'\(')
        self.lexer.add('RPAREN', r'\)')

        # braces
        self.lexer.add('LBRACES', r'\{')
        self.lexer.add('RBRACES', r'\}')

        # Declare Operator
        self.lexer.add('DEC_OP', r'::')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Coma
        self.lexer.add('COMA', r'\,')

        # Arithmetic Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')

        # Relational Operators
        self.lexer.add('LESS_EQUAL', r'<=')
        self.lexer.add('GREATER_EQUAL', r'>=')
        self.lexer.add('LESS_THAN', r'<')
        self.lexer.add('GREATER_THAN', r'>')
        self.lexer.add('NOT_EQUAL_TO', r'!=')
        self.lexer.add('IS_EQUAL', r'==')

        # =
        self.lexer.add('EQUAL', r'\=')

        # and - or
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')

        # if - esle - then 
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('THEN', r'then')

        # Do - while 
        self.lexer.add('WHILE', r'while')
        self.lexer.add('DO', r'do')

        # For
        self.lexer.add('FOR', r'for')

        # Data Types - declaration
        self.lexer.add('DT_INT', r'int')
        self.lexer.add('DT_STRING', r'string')
        self.lexer.add('DT_REAL', r'real')
        self.lexer.add('DT_BOOLEAN', r'bool')

        # Data Types - values
        self.lexer.add('REAL',  r"\d+(\.\d+)")
        self.lexer.add('INT', r'\d+')
        self.lexer.add('STRING', r'".*"')
        self.lexer.add('BOOLEAN', r"(true|false)")

        # IDs - Vars
        self.lexer.add('VAR_NAME', r'[_\w]*[_\w0-9]+')
        
        # Ignore spaces
        self.lexer.ignore('\s+')

        # Ignore comment
        self.lexer.ignore(r'#.*')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()