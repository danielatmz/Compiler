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

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Coma
        self.lexer.add('COMA', r'\,')

        # dot
        self.lexer.add('DOT', r'\.')

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

        # Number
        self.lexer.add('NUMBER', r'\d+')
        
        # Ignore spaces
        self.lexer.ignore('\s+')
        # # Ignore Tab 
        # self.lexer.ignore('\t')
        # # Ignore Linejump 
        # self.lexer.ignore(r'\n')
        



    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()