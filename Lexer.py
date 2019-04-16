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
    'max': 'MAX',
    'define': 'DEFINE',
    'create': 'CREATE',
    'tester': 'TESTER'

}

tokens = [
    'ID',
    'NUM',
    'STRING',
    'OPENPAR',
    'CLOSEPAR',
    'OPENBRACKET',
    'CLOSEBRACKET',
    'OPENCURLY',
    'CLOSECURLY'
    'COLON'

] + list(reserved.values())

#rules for regular expressions

#parenthesis
t_OPENPAR= r'\('
t_CLOSEPAR= r'\)'

#brackets
t_OPENBRACKET= r'\['
t_CLOSEBRACKET= r'\]'

#curly
t_OPENCURLY= r'\{'
t_CLOSECURLY= r'\}'

#colon
t_COLON= r'\;'


#numbers
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t
#ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

#line number?
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#espacios y tabs
t_ignore  = ' \t'

#error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#build the lexer
lexer = lex.lex()
