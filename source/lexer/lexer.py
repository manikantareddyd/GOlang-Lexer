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
            Toks[tok.type][1]=Toks[tok.type][1]+1
            if tok.value in Toks[tok.type]: continue
            Toks[tok.type].append(tok.value)

       	for x in Toks:
            if Toks[x][1]!=0 :
                print "-"*32
                print Toks[x][0],"\n\t",Toks[x][1],"\t",Toks[x][2]
                for i in range(3,len(Toks[x])):
                    print "\t\t",Toks[x][i]

        print "-"*32,'\nIllegal list'
        for i in range(0,len(ERROR_LIST)):
            print ERROR_LIST[i]+"\t",
        print "\n","-"*32

except IOError as e:
    print "I/O error({0}): "+ "We are not able to open " + file_name + " . Does it Exists? Check permissionsi!"
