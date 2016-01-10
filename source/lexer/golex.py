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


#These are a set of reserved tokens in GO, NOT to be used as keywords
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
        'MOD',
        'AMPERS',
        'OR',
        'CARET',
        'LL',
        'GG',
        'AMPCAR',
        'MINUSEQ',
        'DIVIDEEQ',
        'MODEQ',
        'AMPEQ',
        'OREQ',
        'CAREQ',
        'LLEQ',
        'GGEQ',
        'AMPCAREQ',
        'AMPAMP',
        'OROR',
        'LMINUS',
        'PLUSPLUS',
        'MINUSMIN',
        'EQEQ',
        'LESS',
        'GREAT',
        'EQUAL',
        'NOT',
        'NOTEQ',
        'LEQ',
        'GEQ',
        'COLONEQ',
        'DDD',
        'LPAREN',
        'RPAREN',
        'LBRACK',
        'RBRACK',
        'LBRACE',
        'RBRACE',
        'COMMA',
        'DOT',
        'SEMICOL',
        'COLON',
        'IDENTIFIER', 
        'PLUSEQ',
        'TIMESEQ'  
        ] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_AMPERS  = r'&'
t_OR 	  = r'\|'
t_CARET   = r'\^'
t_LL      = r'<<'
t_GG	  = r'>>'
t_AMPCAR  = r'&\^'
t_PLUSEQ  = r'\+='
t_MINUSEQ = r'-='
t_TIMESEQ = r'\*='
t_DIVIDEEQ= r'/='
t_MODEQ   = r'%='
t_AMPEQ   = r'&='
t_OREQ    = r'\|='
t_CAREQ   = r'\^='
t_LLEQ    = r'<<='
t_GGEQ    = r'>>='
t_AMPCAREQ= r'&\^='
t_AMPAMP  = r'&&'
t_OROR    = r'\|\|'
t_LMINUS  = r'<-'
t_PLUSPLUS= r'\+\+'
t_MINUSMIN= r'--'
t_EQEQ    = r'=='
t_LESS    = r'<'
t_GREAT   = r'>'
t_EQUAL   = r'='
t_NOT     = r'!'
t_NOTEQ   = r'!='
t_LEQ     = r'<='
t_GEQ     = r'>='
t_COLONEQ = r':='
t_DDD	  = r'\.\.\.'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACK  = r'\['
t_RBRACK  = r'\]'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COMMA   = r'\,'
t_DOT     = r'\.'
t_SEMICOL = r'\;'
t_COLON   = r'\:'  



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
