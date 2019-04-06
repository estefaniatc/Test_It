import ply.lex as lex
import ply.yacc as yacc

tokens = [

]

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

