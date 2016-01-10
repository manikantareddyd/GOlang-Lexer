# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore_COMMENT = r'(?://[^\n]*|/\*(?:(?!\*/).)*\*/)'

reserved = {
        'break':'BREAK',
        'default':'DEFAULT',
        'func':'FUNCTION',
        'interface':'INTERFACE',
        'select':'SELECT',
        'case':'CASE',
        'defer':'DEFER',
        'go':'GO',
        'map':'MAP',
        'struct':'STRUCT',
        'chan':'CHAN',
        'else':'ELSE',
        'goto':'GOTO',
        'package':'PACKAGE',
        'switch':'SWITCH',
        'const':'CONSTANT',
        'fallthrough':'FALLTHROUGH',
        'if':'IF',
        'range':'RANGE',
        'type':'TYPE',
        'continue':'CONTINUE',
        'for':'FOR',
        'import':'IMPORT',
        'return':'RETURN',
        'var':'VAR'
        }
# List of token names.   This is always required
tokens = [
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
        'LPAREN',
        'RPAREN',
        'IDENTIFIER',   
        ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


def t_IDENTIFIER(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()
