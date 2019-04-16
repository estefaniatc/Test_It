import ply.lex as lex
import ply.yacc as yacc


reserved = {
    'test': 'TEST',
    'method': 'METHOD',
    'input': 'INPUT',
    'expected': 'EXPECTED',
    'output': 'OUTPUT',
    'execute': 'EXECUTE',
    'void': 'VOID',
    'create': 'CREATE',
    'testAll': 'TESTALL',
    'sorted': 'SORTED',
    'negative': 'NEGATIVE',
    'positive': 'POSITIVE',
    'reverse': 'REVERSE',
    'min': 'MIN',
    'max': 'MAX'
}

tokens = [
    'ID',
    'NUM',
    'STRING',
    'OPENPAR',
    'CLOSEPAR',
    'OPENBRACKET',
    'CLOSEBRACKET',
    'COLON'
] + list(reserved.values())

#rules for regular expressions

#parenthesis
t_OPENPAR= r'\('
t_CLOSEPAR= r'\)'

#numbers
#words not reserved
#line numbers?
#error handling
#build the lexer


#custom tester

#tester
def t_TESTER(t):
    reserved.get(t.value, "METHOD")
    t.typer = reserved.get(t.value, "STRING")
