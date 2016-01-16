import sys
import ply.lex as lex
from regexes import *

Toks={}
for a in tokens:
    Toks[a]=[a,0]

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
        print '\n'
        NoOfTok=0
        for tok in lexer:
            lis = Toks[tok.type]
            lis[1]=lis[1]+1
            lis.append(tok.value)
            Toks[tok.type]=lis
              
       	for x in Toks:
            lis=Toks[x]
            if lis[1]!=0 :
                print lis[0],lis[1],lis[2:]

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"
