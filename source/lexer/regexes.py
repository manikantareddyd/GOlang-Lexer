from tokens import *

# Regular expression rules for simple tokens

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Comments
t_ignore_COMMENT = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'

#Identifier token for names and variables
def t_IDENTIFIER(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
        return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
