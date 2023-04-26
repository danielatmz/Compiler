from rply import ParserGenerator
from ast_1 import *


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['REAL', 'INT', 'STRING', 'BOOLEAN',
             
             'DT_REAL', 'DT_INT', 'DT_STRING', 'DT_BOOLEAN',
             
             'LPAREN', 'RPAREN', 'LBRACES', 'RBRACES', 
             'DEC_OP', 'COMA',
             
             'SUM', 'SUB', 'MULT', 'DIV',
             'LESS_EQUAL', 'GREATER_EQUAL', 'LESS_THAN', 'GREATER_THAN',
             'NOT_EQUAL_TO', 'IS_EQUAL', 'EQUAL',

             'PRINT', 'AND', 'OR', 'VAR_NAME',

             'PROGRAM', 'MAIN', 'END'],
            # A list of precedence rules with ascending precedence, to
            # disambiguate ambiguous production rules.
            precedence = [
            ('left', ['LESS_THAN', 'GREATER_THAN']),
            ('left', ['LESS_EQUAL', 'GREATER_EQUAL']),
            ('left', ['IS_EQUAL', 'NOT_EQUAL_TO']),
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV']),
            ]
        )

    def parse(self):
        # main program
        @self.pg.production("program : PROGRAM MAIN statements END PROGRAM MAIN")
        def program(p):
            return p[2]

        @self.pg.production("statements : statements statements")
        @self.pg.production("statements : proc")
        @self.pg.production("statements : expression")
        def statements_all(p):
            return Statements(p)
        
        # Declaration - int :: x
        @self.pg.production('VAR_LIST : VAR_NAME')
        def varDeclaration(p):
            return [p[0].getstr()]
        
        @self.pg.production('VAR_LIST : VAR_NAME COMA VAR_LIST')
        def varDeclarationList(p):
            return [p[0].getstr()] + p[2]

        @self.pg.production('proc : dataType DEC_OP VAR_LIST')
        def varDec(p):
            VAR_LIST = p[2]
            print(p[2])
            for n in VAR_LIST:
                return Declare(n)
        
        #assignation - x = 2
        @self.pg.production('proc : VAR_NAME EQUAL expression')
        def varAssign(p):
            return Assign(p[0].getstr(), p[2])
        
        @self.pg.production('expression : VAR_NAME')
        def id(p):
            return Variable(p[0].getstr())
        
        # print
        @self.pg.production('proc : PRINT expression')
        def proc(p):
            if len(p) > 1:
                return Print(p[1])
            else:
                return p[0]
        
        # paren
        @self.pg.production('expression : LPAREN expression RPAREN')
        def expression_parenths(p):
            return p[1]

        # arithmetic operations
        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        def expression_arithmetics(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            
        # relational operations
        @self.pg.production('expression : expression LESS_EQUAL expression')
        @self.pg.production('expression : expression GREATER_EQUAL expression')
        @self.pg.production('expression : expression LESS_THAN expression')
        @self.pg.production('expression : expression GREATER_THAN expression')
        @self.pg.production('expression : expression NOT_EQUAL_TO expression')
        @self.pg.production('expression : expression IS_EQUAL expression')
        def expression_relationals(p):
            left = p[0]
            right = p[2]
            relOperator = p[1]
            if relOperator.gettokentype() == 'LESS_EQUAL':
                return LessEqual(left, right)
            elif relOperator.gettokentype() == 'GREATER_EQUAL':
                return GreaterEqual(left, right)
            elif relOperator.gettokentype() == 'LESS_THAN':
                return LessThan(left, right)
            elif relOperator.gettokentype() == 'GREATER_THAN':
                return GreaterThan(left, right)
            elif relOperator.gettokentype() == 'NOT_EQUAL_TO':
                return NotEqualTo(left, right)
            elif relOperator.gettokentype() == 'IS_EQUAL':
                return IsEqual(left, right)
        
        #Datatypes: 
        @self.pg.production('dataType : DT_INT')
        @self.pg.production('dataType : DT_STRING')
        @self.pg.production('dataType : DT_REAL')
        @self.pg.production('dataType : DT_BOOLEAN')
        def dataTypes(p):
            return p[0]
        
        
        # NUMBER/INT expressions
        @self.pg.production('expression : REAL')
        @self.pg.production('expression : INT')
        def number(p):
            if (p[0].gettokentype() == 'REAL'):
                return Real(p[0].value)
            return Number(p[0].value)
        
        # STRING expressions
        @self.pg.production('expression : STRING')
        def string(p):
            return String(p[0].value[1:-1])

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()