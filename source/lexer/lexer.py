import sys
import ply.lex as lex
from regexes import *


#Scanning the file name
if (len(sys.argv) == 1):
    file_name =raw_input( "Give a GO file to lexer: ")
else:
    file_name = sys.argv[1]

try:
    lexer = lex.lex()
    with open(file_name) as fp:#opening file
        data = fp.read()
        data += '\n'
        lexer.input(data)
       	for tok in lexer:
       		print tok
            
except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"
